#ifndef STACK_H
#define STACK_H

#include <stddef.h>
#include <stdbool.h>

#ifdef __cplusplus
extern "C" {
#endif

/* Dynamic-array based LIFO stack of int */
typedef struct {
    int    *data;  /* contiguous storage */
    size_t  size;  /* current number of elements */
    size_t  cap;   /* allocated capacity */
} Stack;

/* Initialize the stack. If init_cap == 0, a default (16) is used. */
bool   stack_init(Stack *s, size_t init_cap);

/* Release all resources held by the stack. Safe to call on an empty stack. */
void   stack_free(Stack *s);

/* Return true if the stack contains no elements. */
bool   stack_empty(const Stack *s);

/* Return the number of elements currently stored. */
size_t stack_size(const Stack *s);

/* Push one element (amortized O(1)). Returns false on allocation failure. */
bool   stack_push(Stack *s, int x);

/* Pop the top element into *out (if non-NULL). Returns false if empty. */
bool   stack_pop(Stack *s, int *out);

/* Read the top element into *out (if non-NULL). Returns false if empty. */
bool   stack_top(const Stack *s, int *out);

#ifdef __cplusplus
}
#endif

#endif /* STACK_H */
