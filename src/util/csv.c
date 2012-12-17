/*
 * CSV Reader
 *
 *  Author: Sean Allred
 * Version: 12 December 2012
 * Purpose: Allows basic interaction with CSV files
 *         (or those in the CSV format).
 *
 * The content of this file is released under the GNU GPLv3.
 */

#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include <string.h>
#include "csv.h"

#define NEWLINE '\n'

CSVReaderRef* __CLASS__CSV_READER__ALLOC(void)
{
    return (CSVReaderRef *)(malloc(sizeof(struct __CLASS__CSV_READER__MODEL)));
}

void __CLASS__CSV_READER__DEALLOC(CSVReaderRef *obj)
{
    // Free all the data
    // Potential bug: row-major vs col-major (C is row-major)
    for(int i = 0; i < obj->_rowCount; i++)
    {
        for(int j = 0; j < obj->_colCount; j++)
        {
            free(obj->data[i][j]);
        }
        free(obj->data[i]);
    }
    free(obj->data);

    // Free the object itself
    free(obj);
}

void __CLASS__CSV_READER__INIT(CSVReaderRef *obj)
{
    obj->data = NULL;
    obj->_source = NULL;
    obj->_colCount = obj->_rowCount = -1;
}

// We should probably have some sort of NEWLINE_SEQUENCE constant
int __CLASS__CSV_READER__READ(CSVReaderRef *obj, char *path, char delim)
{

    obj->_source = path;

    FILE *f; // The file we are reading
    long fSize; // The size of the file (determined by fseek)
    char *buffer; // the location of raw data
    size_t sizeRead; // the actual number of bytes read from f
    if (f = fopen(obj->_source, "r"))
    {
        if (f == NULL)
        {
            // Some file error occurred
            return -2;
        }

        // Determine the size of the file
        {
            fseek(f, 0, SEEK_END);
            fSize = ftell(f);
            rewind(f);
        }

        // Allocate enough memory to store the contents of the file
        buffer = (char*) malloc (sizeof(char) * fSize);

        if (buffer == NULL)
        {
            // Some memory error occurred, most likely not enough of it
            return -3;
        }

        // Read the entire file into the buffer
        sizeRead = fread(buffer, 1, fSize, f);

        if (sizeRead != fSize)
        {
            // We didn't read as many bytes as we thought we would!!
            return -4;
        }
        /* the whole file is now loaded into `buffer' */

        // Count the number of commas up to a newline,
        // then count the number of newlines.
        // We now have the number of rows and the number of columns.

        /// while current_char != \n
        ///     if current_char is ','
        ///         ncomma++
        ///     current_char++

        // or something like that
        {
            // Determine the dimensions of the CSV
            // TODO: theoretically breaks when there is only one line in the file
            char *currentChar = buffer;
            int position = 0;
            obj->_colCount = obj->_rowCount = 1;

            while(currentChar[position] != NEWLINE && position != fSize)
            {
                if (currentChar[position] == delim)
                {
                    (obj->_colCount)++;
                }
                position++;
            }

            while(position < fSize)
            {
                if (currentChar[position] == NEWLINE && (position != fSize - 1))
                {
                    (obj->_rowCount)++;
                }
                position++;
            }
        }

        /* We now know how many rows and columns the file is */

        // Fill data from the file.
        /// ? Can we use strtok instead?
        {
            int wordSize;
            char *currentChar = buffer;
            // Allocate memory for an array of string arrays of _rowCount length
            obj->data = (char ***)(malloc(sizeof(char **) * obj->_rowCount));

            for (int r = 0; r < obj->_rowCount; r++)
            {
                // Allocate memory for this string array
                obj->data[r] = (char**)(malloc(sizeof(char*) * obj->_colCount));
                //char *row = strtok

                for (int c = 0; c < obj->_colCount; c++)
                {
                    wordSize = 0;
                    while(*currentChar != NEWLINE && *currentChar != EOF && *currentChar != delim)
                    {
                            wordSize++;
                            currentChar++;
                    }

                    obj->data[r][c] = (char*)(malloc(sizeof(char) * wordSize));

                    //Populates the word with data
                    for(int w = 0; w < wordSize; w++)
                            obj->data[r][c][w] = *(currentChar - wordSize + w);

                    if(*currentChar != EOF)
                        currentChar++;
                }
            }
        }

        fclose(f);
        return 0;
    }
    return -1; // The file was unable to be read (probably didn't exist)
}


void **__CLASS__CSV_READER__PARSE(CSVReaderRef *obj, void* (*parser)(char**), size_t size)
{
    // Allocate enough memory to store each object
    void **objects = (void**)malloc(size * obj->_rowCount);

    // Apply the parser
    for (int i = 0; i < obj->_rowCount; i++)
    {
        objects[i] = parser(obj->data[i]);
    }

    // and return the collection
    return objects;
}

void __INIT__CSV_READER(CSVReader *reader)
{
    (*reader).alloc = &__CLASS__CSV_READER__ALLOC;
    (*reader).dealloc = &__CLASS__CSV_READER__DEALLOC;
    (*reader).init = &__CLASS__CSV_READER__INIT;
    (*reader).read = &__CLASS__CSV_READER__READ;
    (*reader).parse = &__CLASS__CSV_READER__PARSE;
}
