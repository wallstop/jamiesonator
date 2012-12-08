//
//  LinkedList.c
//  bits
//
//  Created by Sean Allred on 7/18/12.
//  Copyright (c) 2012 St. Mary's College of Maryland. All rights reserved.
//

#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include "csv.h"

CSVReaderRef __CLASS__CSV_READER__METHODS__ALLOC() {
    return malloc(sizeof(struct __CLASS__CSV_READER__MODEL));
}

void __CLASS__CSV_READER__METHODS__DEALLOC(CSVReaderRef obj) {
    // Make sure the file is closed
    // ??
    
    // Free all the data
    for(int i = 0; i < _row_count; i++) {
        for(int j = 0; j < _col_count; j++) {
            free(data[i][j]);
        }
        free(data[i]);
    }
    free(data);
    
    // Free the object itself
    free(obj);
}

void __CLASS__CSV_READER__METHODS__INIT(CSVReaderRef obj) {
    // What needs to be done?
}

// We should probably have some sort of NEWLINE_SEQUENCE constant
int __CLASS__CSV_READER__METHODS__SET_SOURCE(CSVReaderRef obj, const char *path) {
    FILE *f; // The file we are reading
    long f_size; // The size of the file (determined by fseek)
    char *buffer; // the location of raw data
    size_t size_read; // the actual number of bytes read from f
    if (f = fopen(path, "r")) {
        if (f == NULL) {
            // Some file error occurred
            return -2;
        }
        long f_size;
        char *buffer;
        {
            fseek(f, 0, SEEK_END);
            f_size = ftell(f);
            rewind(f);
        }
        
        buffer = (char*) malloc (sizeof(char) * f_size);
        
        if (buffer == NULL) {
            // Some mememory error occurred, most likely not enough mem
            return -3;
        }
        
        size_read = fread(buffer, 1, f_size, f);
        
        if (result != f_size) {
            // We didn't read as many files as we thought we would!!
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
        
        fclose(f);
        return 0;
    }
    return -1; // The file was unable to be read (probably didn't exist)
    
}
  // Sets the source of this CSVReader.
	// If no file exists at the given path,
	// the return value is -1, 0 otherwise.
	int (*set_source)(CSVReaderRef, const char *);

	// Reads the source file and places
	// read information into `data'
	void (*read)(CSVReaderRef);