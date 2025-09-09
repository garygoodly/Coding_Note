#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include "General.h"
#include "Gstring.h"

void reverse_string(char* str) {
    int i = 0;
    for (; str[i] != '\0'; i++);
    for (int j = 0; j < i / 2; j++)
        swap_char(&str[j], &str[i - 1 - j]);
}

void space_remove(char* str) {
    int l = 0, r = strlen(str) - 1;
    while (str[l] == ' ') l++;
    while (str[r] == ' ') r--;
    int slow = 0;
    bool flag = 0;
    while (l <= r) {
        printf("%c", str[l]);
        if (str[l] == ' ') {
            flag = 1;
        }
        else {
            if (flag)
                str[slow++] = ' ';
                flag = 0;
            str[slow++] = str[l];

        }
        l++;
    }
    str[slow] = '\0';
}

void reverse_string_partial(char*str, int start, int end) {
    for (int j = start; j < (start + end + 1) / 2; j++)
        swap_char(&str[j], &str[end + start - j]);
}

void* reverseWords(char* s) {
    reverse_string(s);
    space_remove(s);
    int l = 0, r = 0, len = strlen(s);
    while (r < len) {
        if (r == ' ') {
            reverse_string_partial(s, l, r++);
            l = r;
        }
        else r++;
    }
    reverse_string_partial(s, l, r - 1);
    return s;
}

void common_fix_length(char* p, int* arr, int n) {
    int len = 0;
    arr[0] = 0;
    for (int i = 1; i < n;) {
        if (p[i] == p[len])
            arr[i++] = ++len; 
        else if (len > 0) 
            len = arr[len - 1];
        else
            arr[i++] = len;
    }
}

int strStr(char* haystack, char* needle) {
    int n = strlen(needle);
    int* maxCommon = (int *)malloc(strlen(needle) *sizeof(int));
    common_fix_length(needle, maxCommon, n);
    int i = 0, j = 0;
    while (haystack[i] != '\0') {
        if (haystack[i] == needle[j]) {
            i++; j++;
            if (j == n)
                return i - n;
        }
        else {
            if (j) j = maxCommon[j - 1];
            else i++;
        }
    }
    return -1;
}

bool repeatedSubstringPattern(char* s) {
    int n = strlen(s);
    int* arr = (int *)malloc(n * sizeof(int));
    common_fix_length(s, arr, n);
    return n % (n - arr[n - 1]) == 0;
}