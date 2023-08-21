#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/*
This section of the code includes necessary C standard library headers:
stdio.h: Standard I/O functions, used for input and output operations.
stdlib.h: Standard library functions, used for memory allocation and other general utilities.
string.h: String manipulation functions, used for working with strings.
*/

int main() {
    char *dir = ".";
    char *ext = strrchr(dir, '.');

    if (ext != NULL && strcmp(ext, ".out") == 0) {
        char command[256];
        snprintf(command, sizeof(command), "./%s", dir);
        system(command);
    }

    return 0;
}

/*
In this version of the program, snprintf is used to create a string that includes ./ before the file name. This string is then passed to 
system, so it executes the file in the current directory.
*/
