// gcc main.c -o ../out/dont_dead_open_inside -z execstack -no-pie
#include <stdio.h>
#include <stddef.h>
#include <stdlib.h>
#include <unistd.h>

#include <sys/prctl.h>
#include <linux/seccomp.h>
#include <linux/filter.h>
#include <linux/audit.h>
#include <sys/syscall.h>

static long syscalls[] = {
    SYS_open, SYS_openat, SYS_mq_open, SYS_perf_event_open, SYS_open_by_handle_at
};

void setup()
{
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stdin, NULL, _IONBF, 0);

    prctl(PR_SET_NO_NEW_PRIVS, 1, 0, 0, 0);

    unsigned long SYSCALLS_LEN  = sizeof(syscalls)/sizeof(syscalls[0]);
    unsigned long NUM_INSTRS    = SYSCALLS_LEN + 5;
    unsigned long FAIL_IDX      = NUM_INSTRS-1;
    unsigned long ACCEPT_IDX    = NUM_INSTRS-2;

    struct sock_filter instrs[NUM_INSTRS];
    instrs[0] = (struct sock_filter)BPF_STMT(BPF_LD | BPF_W | BPF_ABS, offsetof(struct seccomp_data, arch));
    unsigned int my_arch = AUDIT_ARCH_X86_64;
    instrs[1] = (struct sock_filter)BPF_JUMP(BPF_JMP | BPF_JEQ | BPF_K, my_arch, 0, FAIL_IDX-(1+1));
    instrs[2] = (struct sock_filter)BPF_STMT(BPF_LD | BPF_W | BPF_ABS, offsetof(struct seccomp_data, nr));
    for (int i=0; i<SYSCALLS_LEN; i++) {
        instrs[i+3] = (struct sock_filter)BPF_JUMP(BPF_JMP | BPF_JEQ | BPF_K, syscalls[i], FAIL_IDX-(i+3+1), 0);
    }
    instrs[ACCEPT_IDX] = (struct sock_filter)BPF_STMT(BPF_RET | BPF_K, SECCOMP_RET_ALLOW);
    instrs[FAIL_IDX]   = (struct sock_filter)BPF_STMT(BPF_RET+BPF_K, SECCOMP_RET_KILL);
    struct sock_fprog fprog = {.len = NUM_INSTRS, .filter = instrs};
    prctl(PR_SET_SECCOMP, SECCOMP_MODE_FILTER, &fprog, 0, 0);
}

int main()
{
    char shellcode[1024];

    setup();
    printf("Just read /dont_dead_open_inside_flag.txt\nEnter shellcode: ");
    
    read(STDIN_FILENO, shellcode, sizeof(shellcode));
    ((void (*) (void)) shellcode) ();

    return EXIT_SUCCESS;
}
