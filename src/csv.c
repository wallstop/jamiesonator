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
//#include "csv.h"
typedef void * CSVReaderRef; // We need to resolve this include business ASAP. I'll post something on SO.

CSVReaderRef __CLASS__CSV_READER__METHODS__ALLOC() {
    return malloc(sizeof(struct __CLASS__LINKEDLIST__MODEL));
}