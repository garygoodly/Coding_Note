#include <stdio.h>
#include <stdlib.h>

int main() {
    int a = 5, b = 3;
    a ^= b ^= a ^= b;
    printf("%d %d", a, b);
    return 0;
}