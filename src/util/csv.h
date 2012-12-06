/*
 * CSV Reader
 *
 *  Author: Sean Allred
 * Version: 5 December 2012
 * Purpose: Allows basic interaction with CSV files
 *         (or those in the CSV format).
 *
 * The content of this file is released under the GNU GPLv3.
 */

/* TODO:
 * 		applies a specialized parsing function per-record
			void* (*parse)(CSVReaderRef, (void*)(*parser)(char**), size_t)
			takes a full row of data and parses
 */
 
#ifndef __CLASSDEF__CSV_READER_H
#define __CLASSDEF__CSV_READER_H

typedef struct __STRUCT__CSV_READER__MODEL * CSVReaderRef;
 
struct __STRUCT__CSV_READER__MODEL {
	char * _source; // The current path of the CSV file of interest
	char *** data; // a matrix of strings - an array of arrays of arrays of characters.
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
	int (*set_source)(CSVReaderRef, const char *);
	
	// Reads the source file and places
	// read information into `data'
	void (*read)(CSVReaderRef);
} CSVReader;

#endif
