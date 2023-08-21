// clipbridge.c
#include <stdio.h>

int main() {
  char buffer[1024];
  fgets(buffer, sizeof(buffer), stdin);  
  system("clip.exe < /dev/stdin"); 
  return 0;
}
    
    
/*    Compile it: gcc -o clipbridge clipbridge.c
    Then you can pipe to it:
        cat file.txt | ./clipbridge */