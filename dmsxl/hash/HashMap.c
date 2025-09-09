#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>
#include <stdint.h>
// #include "HashMap.h"

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>
#include <stdint.h>
// #include "HashMap.h"

bool isAnagram(char* s, char* t) {
    if (strlen(s) != strlen(t)) return false;

    uint16_t count[26] = {0};
    for (uint16_t i = 0; s[i] != '\0'; i++)
        count[s[i] - 'a'] += 1;
    
    for (uint16_t i = 0; t[i] != '\0'; i++) {
        if (count[t[i] - 'a'] == 0) 
            return false;
        count[t[i] - 'a'] -= 1;
    }
    return true;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
void minHash(int* h1, int* h2) {
    for (int i = 0; i < 26; i++) {
        h1[i] = h1[i] < h2[i] ? h1[i] : h2[i];
        h2[i] = 0;
    }
}

char** commonChars(char** words, int wordsSize, int* returnSize) {
    *returnSize = 0;
    int hash1[26] = {0};
    int hash2[26] = {0};

    for (int i = 0; words[0][i] != '\0'; i++)
        hash1[words[0][i]  - 'a']++;
    
    for (int j = 1; j < wordsSize; j++) {
        for (int i = 0; words[j][i] != '\0'; i++)
            hash2[words[j][i]  - 'a']++;
        minHash(hash1, hash2);        
    }

    char** ans = (char **)malloc(sizeof(char *) * 100);
    for (int i = 0; i < 26; i++) {
        for (int j = 0; j < hash1[i]; j++) {
            char* str = (char *)malloc(sizeof(char) * 2);
            str[0] = i + 'a';
            str[1] = '\0';
            ans[(*returnSize)++] = str;
        }
    }
    return ans;
}

bool isHappy(int n) {
    bool Visit[163] = {0};
    n = get_sum(get_sum(get_sum(n)));

    while (n != 1) {
        if (Visit[n]) return false;
        n = get_sum(n);
    }
    return true;
}

int get_sum(int n) {
    int sum = 0;
    while (n > 0) {
        sum += (n % 10) * (n % 10);
        n /= 10;
    }
    return sum;
}
