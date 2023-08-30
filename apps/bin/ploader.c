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
