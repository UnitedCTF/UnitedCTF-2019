#include <stdio.h>
#include <string.h>

void print_yellow(char* str) {
    printf("\033[33;1m%s\033[0m", str);
}

void print_red(char* str) {
    printf("\033[31m%s\033[0m", str);
}

void print_green(char* str) {
    printf("\033[92m%s\033[0m", str);
}

int main() {
    char* header = "Welcome to FAST, the Flag Assertion Service for Terminals\n";
    unsigned char flag[] = {
        70,
        77,
        67,
        74,
        49,
        124,
        110,
        59,
        124,
        104,
        62,
        106,
        121,
        64,
        129,
        130,
        26
    };
    print_yellow(header);
    printf("Please enter flag to validate!\n");

    char input[20];
    fgets(input,20,stdin);

    for (int i = 0; i < strlen(input); i++) {
        unsigned char c = input[i] + i;
        if (c != flag[i]) {
            print_red("Invalid flag, better luck next time!");
            return 1;
        }
    }
    print_green("Flag validated! Congratulations :D");
}
