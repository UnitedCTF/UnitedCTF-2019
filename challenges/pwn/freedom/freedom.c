#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

char* graphics[] = {
    "cat eagles/1",
    "cat eagles/2",
    "cat eagles/3",
};

typedef struct eagle {
    char name[16];
    int type;
} eagle;

eagle* eagles[] = {
    NULL,
    NULL,
    NULL
};

int read_int(const char* prompt) {
    char input[32];
    printf("%s\n", prompt);
    scanf("%31s", input);

    return atoi(input);
}

int menu() {
    char input[32] = {0};

    printf("===============\n");
    printf("1. Create eagle\n");
    printf("2. Rename eagle\n");
    printf("3. Free eagle\n");
    printf("4. Exit\n");
    return read_int("> Your choice:");
}

int main(int argc, char* argv[]) {
    setbuf(stdin, NULL);
    setbuf(stdout, NULL);

    while(1) {
        int choice = menu();

        if(choice == 4) {
            exit(0);
        } else if(choice < 1 || choice > 4) {
            continue;
        }

        int eagle_number = read_int("Eagle number (1, 2 or 3):");
                
        if(eagle_number < 1 || eagle_number > 3) {
            printf("Invalid number!\n");
            continue;
        }

        switch(choice) {
            case 1: {
                int type = read_int("Eagle type (1, 2 or 3):");

                if(type < 1 || type > 3) {
                    printf("Invalid type!\n");
                    break;
                }

                eagle* e = malloc(sizeof(eagle));
                strcpy(e->name, "America");
                e->type = type;

                eagles[eagle_number - 1] = e;

                system(graphics[type - 1]);
                break;
            }
            
            case 2: {
                printf("New name:\n");
                read(0, eagles[eagle_number - 1]->name, 8);
                break;
            }
            
            case 3: {
                eagle* e = eagles[eagle_number - 1];
                printf("Be free, %s, you majestic beast!\n", e->name);
                free(e);
                break;
            }
        }
    }

    return 0;
}