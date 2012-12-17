#include <stdio.h>
#include <stdlib.h>

// I can't for the life of me figure out how to add the damn header file
// with a relative path. Any wisdom on that end?
#include "util/csv.h"


void _AnyKey(void);


//int main(int argc, char **argv) {
int main(void) {
    puts("hello, world");

    char *filepathbuf = (char*)malloc(sizeof(char)*256);
    memset(filepathbuf, 0, 256);

    printf("Enter a file path (absolutely!!! MUAHAHA):");
    scanf("%s", filepathbuf);
    printf("You entered %s. Beginning test.\n", filepathbuf);

    CSVReader tempReader;

    __INIT__CSV_READER(&tempReader);
    CSVReaderRef *myReader = tempReader.alloc();
    tempReader.init(myReader);
    tempReader.read(myReader, filepathbuf, ',');

    for (int r = 0; r < myReader->_rowCount; r++)
    {
        for (int c = 0; c < myReader->_colCount; c++)
        {
            printf("%s ", myReader->data[r][c]);
        }
        printf("\n");
    }

    printf("Test complete.");

    _AnyKey();
    return 0;
}

void _AnyKey(void) {
    printf("Press enter to continue...");
    getchar();
}
