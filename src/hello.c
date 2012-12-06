#include <stdio.h>

// I can't for the life of me figure out how to add the damn header file
// with a relative path. Any wisdom on that end?
#include </#_/Programming/GitHub/jamiesonator/src/util/csv.h>


void _AnyKey(void);


//int main(int argc, char **argv) {
int main(void) {
    puts("hello, world");
    _AnyKey();
    return 0;
}

void _AnyKey(void) {
    printf("Press enter to continue...");
    getchar();
}