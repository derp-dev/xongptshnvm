#include <python.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int is_python_file(char *filename)
{
  int len = strlen(filename);
  if (len < 4)
    return 0;
  if (filename[len - 3] == '.' && filename[len - 2] == 'p' && filename[len - 1] == 'y')
    return 1;
  return 0;
}

int main(int argc, char *argv[])
{
  if (argc < 2)
  {
    printf("Usage: ploader <python file>\n");
    return 0;
  }
  if (!is_python_file(argv[1]))
  {
    printf("Error: %s is not a python file\n", argv[1]);
    return 0;
  }
  FILE *fp = fopen(argv[1], "r");
  if (!fp)
  {
    printf("Error: cannot open %s\n", argv[1]);
    return 0;
  }
  /*It calculates the size of the file by moving the file pointer to the end, determining the position (size), and then moving the file pointer back to the beginning. It allocates memory for a buffer (buf) to store the content of the file, reads the content into the buffer, and adds a null terminator to mark the end of the string. Finally, it closes the file.*/
  fseek(fp, 0, SEEK_END);
  int size = ftell(fp);
  fseek(fp, 0, SEEK_SET);
  char *buf = (char *)malloc(size + 1);
  fread(buf, 1, size, fp);
  buf[size] = 0;
  fclose(fp);
  /*It initializes the Python interpreter using Py_Initialize(), runs the content of the buffer as Python code using PyRun_SimpleString(), and then finalizes the Python interpreter using Py_Finalize(). The memory allocated for the buffer is released with free(buf), and the program returns 0 to indicate successful execution.*/
  Py_Initialize();
  PyRun_SimpleString(buf);
  Py_Finalize();
  free(buf);
  return 0;
}
/*
    Memory Leaks: The code allocates memory for the buf variable using malloc, but there's no guarantee that the Python script will not throw an exception. If an exception occurs before free(buf) is reached, there will be a memory leak. A try...catch mechanism or a cleanup routine would be good to handle such cases.

    Error Handling: The code currently prints error messages to the console, but it might be more user-friendly to print error messages to stderr using fprintf(stderr, ...). Also, consider using appropriate exit codes (non-zero values) to indicate errors, e.g., return 1; instead of return 0;.

    Python Interpreter Initialization and Finalization: It's important to check the return value of Py_Initialize() and handle initialization errors. Similarly, you should also check the return value of PyRun_SimpleString() and any other Python-related function calls for potential errors.

    Security Concerns: Loading and executing arbitrary Python code from an external file can pose security risks. Make sure you're only running code you trust, as malicious code could potentially harm the system.

    Python Environment State: Be aware that running multiple scripts might affect the Python environment state, as Py_Initialize() initializes the Python interpreter, and Py_Finalize() finalizes it. If you're planning to run multiple scripts in succession, consider whether you want to keep the interpreter alive.

    Cross-Platform Considerations: The code seems to be written for a Unix-like environment due to the use of forward slashes for path separation. If you intend for this code to be used on Windows, you should handle path separation using backslashes or a cross-platform approach.
*/