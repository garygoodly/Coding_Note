#include <stdio.h>
#include <stdlib.h>
#include "General.h"


void swap_char(char* a, char* b) {
    char tmp = *a;
    *a = *b;
    *b = tmp;  
};


void swap_int(int* a, int* b) {
    int tmp = *a;
    *a = *b; 
    *b = tmp;
}