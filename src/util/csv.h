/*
 * CSV Reader
 *
 *  Author: Sean Allred
 * Version: 9 December 2012
 * Purpose: Allows basic interaction with CSV files
 *         (or those in the CSV format).
 *
 * The content of this file is released under the GNU GPLv3.
 */

/*  TODO
 *  ====
 * - Add writing functionality
 * 
 */
 
#ifndef __CLASS_DEF__CSV_READER_H
#define __CLASS_DEF__CSV_READER_H

typedef struct __CLASS__CSV_READER__MODEL * CSVReaderRef;
 
struct __CLASS__CSV_READER__MODEL {
	const char * _source; // The current path of the CSV file of interest
	char *** data; // a matrix of strings - an array of arrays of arrays of characters.

    int _row_count;
    int _col_count;
};

struct __CLASS__CSV_READER__METHODS {
	// Creates a new CSVReader.
	CSVReaderRef (*alloc)();
	
	// Frees all memory used by the given CSVReader.
	void (*dealloc)(CSVReaderRef);
	
	// Initializes the given CSVReader.
	void (*init)(CSVReaderRef);
	
	// Sets the source of this CSVReader.
	// If no file exists at the given path,
	// the return value is -1, 0 otherwise.
	// Reads the delimited file and places
	// read information into `data'
	int (*read)(CSVReaderRef, const char *, char);

    // Applies the given parser to each row in the CSV data.
    // This function assumes that data is non-null (that a file has been read)
    // It returns an array of objects produced by subsequent calls to the parser.
    // The last parameter is the size of the produced object.
    void **(*parse)(CSVReaderRef, void* (*parser)(char**), size_t);
} CSVReader;

#endif
