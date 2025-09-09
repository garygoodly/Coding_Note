#include <stdio.h>
#include "General.h"
#include "Gstring.h"

int main() {
    char a = 'a', b = 'b';
    char str1[] = "     aa  bb       eeeeee          ";
    swap_char(&a, &b);
    space_remove(str1);
    printf("%c %c\n", a, b);
    for (int i = 0; str1[i] != '\0'; i++)
        printf("%c", str1[i]);
    return 0;
}