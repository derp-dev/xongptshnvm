#include<stdio.h>

int main() {
    char ch;
    while(1) {
        ch = getchar();
        if (ch == 'Q') {
            ch = getchar();
            if (ch == 'U') {
                ch = getchar();
                if (ch == 'I') {
                    ch = getchar();
                    if (ch == 'T') {
                        break;
                    }
                }
            }
        }
    }
    return 0;
}