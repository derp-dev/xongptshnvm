#include <stdio.h>
#include <stdlib.h>

int main() {
    // Part 1: Array Manipulation using Pointers and Malloc
    double *A = (double *)malloc(4 * sizeof(double));

    if (A == NULL) {
        printf("Memory allocation failed.\n");
        return 1;
    }

    A[0] = 9.0;
    A[1] = 2.9;
    A[2] = 3.E+25;
    A[3] = 0.00007;

    printf("Array Manipulation using Pointers and Malloc:\n");
    for (size_t i = 0; i < 4; ++i) {
        printf("Element %zu is %g,\tits square is %g\n",
               i,
               A[i],
               A[i] * A[i]);
    }

    free(A); // Free allocated memory

    // Part 2: Bitwise Operations
    printf("\nBitwise Operations:\n");
    unsigned char a = 0x53; // 0101 0011 in binary
    unsigned char b = 0xA6; // 1010 0110 in binary

    // Bitwise AND
    unsigned char c = a & b; // 0000 0010 in binary
    printf("a & b = 0x%x\n", c); // output: a & b = 0x2

    // Bitwise OR
    unsigned char d = a | b; // 1111 0111 in binary
    printf("a | b = 0x%x\n", d); // output: a | b = 0xf7

    // Bitwise XOR
    unsigned char e = a ^ b; // 1111 0101 in binary
    printf("a ^ b = 0x%x\n", e); // output: a ^ b = 0xf5

    // Bitwise complement
    unsigned char f = ~a; // 1010 1100 in binary
    printf("~a = 0x%x\n", f); // output: ~a = 0xac

    // Left shift
    unsigned char g = a << 2; // 0101 1100 in binary
    printf("a << 2 = 0x%x\n", g); // output: a << 2 = 0x5c

    // Right shift
    unsigned char h = b >> 3; // 0001 0100 in binary
    printf("b >> 3 = 0x%x\n", h); // output: b >> 3 = 0x14// ... (Same bitwise operations as before)

    return 0;
}
