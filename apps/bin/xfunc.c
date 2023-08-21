#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/* Includes standard library headers for I/O, string handling, general utilities */

#define COMMAND_BUFFER_SIZE 256 

int main() {

  /* Use const since dir is not modified after initialization */
  const char* dir = ".";

  /* Find last occurrence of '.' to get file extension */
  char* ext = strrchr(dir, '.');

  if (ext != NULL && strcmp(ext, ".out") == 0) {
    
    /* Use define for buffer size rather than magic number */
    char command[COMMAND_BUFFER_SIZE];

    /* Append ./ to filename and copy into buffer */
    snprintf(command, COMMAND_BUFFER_SIZE, "./%%s\n", dir);

    /* Execute command using system() */
    system(command);

  }

  return 0;

}

/* Updated version uses define for buffer size, const for immutable variable,
   and adds newline to command string for portability */