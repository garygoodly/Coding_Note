#include "stack.h"
#include <stdlib.h>

bool stack_init(Stack *s, size_t init_cap) {
    if (!s) return false;
    s->size = 0;
    s->cap  = init_cap ? init_cap : 16;
    s->data = (int*)malloc(sizeof(int) * s->cap);
    return s->data != NULL;
}

void stack_free(Stack *s) {
    if (!s) return;
    free(s->data);
    s->data = NULL;
    s->size = 0;
    s->cap  = 0;
}

bool stack_empty(const Stack *s) {
    return !s || s->size == 0;
}

size_t stack_size(const Stack *s) {
    return s ? s->size : 0;
}

bool stack_push(Stack *s, int x) {
    if (!s) return false;
    if (s->size == s->cap) {
        size_t ncap = s->cap ? s->cap * 2 : 16;
        int *p = (int*)realloc(s->data, sizeof(int) * ncap);
        if (!p) return false;   /* keep old buffer intact on failure */
        s->data = p;
        s->cap  = ncap;
    }
    s->data[s->size++] = x;
    return true;
}

bool stack_pop(Stack *s, int *out) {
    if (!s || s->size == 0) return false;
    if (out) *out = s->data[s->size - 1];
    s->size--;
    return true;
}

bool stack_top(const Stack *s, int *out) {
    if (!s || s->size == 0) return false;
    if (out) *out = s->data[s->size - 1];
    return true;
}
