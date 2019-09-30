// gcc main.c -o muted -no-pie
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

struct Contact
{
    char name[32];
    char phone_number[16];
};

static FILE* logfile;
static struct Contact contacts[10];

void log_msg(char* msg)
{
    time_t now = time(NULL);
    char log[1024] = {0};

    strftime(log, sizeof(log), "[%Y-%m-%d %H:%M:%S] ", localtime(&now));
    strncat(log, msg, sizeof(log)-strlen(log)-1);
    fprintf(logfile, log);
    fflush(logfile);
}

void create_contact()
{
    int index = 0;

    while (index < 10) {
        if (*(contacts[index].name) == '\0') {
            break;
        }
        index++;
    }

    if (index == 10) {
        printf("\nYou can't have more than 10 contacts.\n\n");
        return;
    }

    // name
    printf("\nWhat is the contact name?\n> ");
    fgets(contacts[index].name, sizeof(contacts[index].name), stdin);
    contacts[index].name[strcspn(contacts[index].name, "\n")] = 0;

    // phone number
    printf("What is your contact phone number?\n> ");
    fgets(contacts[index].phone_number, sizeof(contacts[index].phone_number), stdin);
    contacts[index].phone_number[strcspn(contacts[index].phone_number, "\n")] = 0;

    log_msg("Contact added.");
    printf("Contact successfully added.\n\n");
}

void view_contacts()
{
    int index;

    printf("\nList of contacts:\n--------------------------------------------------\n");
    for (index = 0; index < 10; index++) {
        if (*(contacts[index].name) != '\0') {
            printf("%d) %s (%s)\n", index+1, contacts[index].name, contacts[index].phone_number);
        }
    }
    printf("--------------------------------------------------\n\n");
}

void delete_contact()
{
    int choice;

    printf("\nWhat contact do you wish to delete?\n> ");
    scanf("%d", &choice);

    if (choice < 1 || choice > 10 || *(contacts[choice-1].name) == '\0') {
        printf("Invalid choice.\n\n");
        return;
    }

    choice--;
    memset(&(contacts[choice]), 0, sizeof(contacts[choice]));

    log_msg("Contact deleted.");
    printf("Contact successfully deleted.\n\n");
}

void report_bug()
{
    char bug[512];
    printf("\nDescribe the bug you found.\n> ");
    fgets(bug, sizeof(bug), stdin);
    log_msg(bug);
    exit(EXIT_SUCCESS);
}

int main(int argc, char* argv[], char* envp[])
{
    int choice = 0;

    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stdin, NULL, _IONBF, 0);
    memset(&contacts, 0, sizeof(contacts));

    if (argc < 2) {
        printf("Usage: ./server LOGFILE\n");
        exit(EXIT_FAILURE);
    }

    logfile = fopen(argv[1], "a");
    if (logfile == NULL) {
        printf("Could not open log file.\n");
        exit(EXIT_FAILURE);
    }

    while(choice != 5) {
        printf("Choose an option:\n1- Create contact\n2- View contacts\n3- Delete contact\n4- Report bug\n5- Exit\n> ");
        scanf("%d", &choice);
        fgetc(stdin);

        switch (choice) {
            case 1: create_contact(); break;
            case 2: view_contacts(); break;
            case 3: delete_contact(); break;
            case 4: report_bug(); break;
        }
    }

    return EXIT_SUCCESS;
}
