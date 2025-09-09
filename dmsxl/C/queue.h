#ifndef QUEUE_H
#define QUEUE_H

#include <stddef.h>
#include <stdbool.h>

#ifdef __cplusplus
extern "C" {
#endif

/* Circular-buffer based FIFO queue of int */
typedef struct {
    int    *data;  /* ring storage */
    size_t  head;  /* index of the current front element (valid when size > 0) */
    size_t  size;  /* number of elements currently stored */
    size_t  cap;   /* capacity (number of elements the buffer can hold) */
} Queue;

/* Initialize the queue. If init_cap == 0, a default (16) is used. */
bool   queue_init(Queue *q, size_t init_cap);

/* Release all resources held by the queue. Safe to call on an empty queue. */
void   queue_free(Queue *q);

/* Return true if the queue contains no elements. */
bool   queue_empty(const Queue *q);

/* Return the number of elements currently stored. */
size_t queue_size(const Queue *q);

/* Enqueue one element at the back (amortized O(1)). Returns false on alloc fail. */
bool   enqueue(Queue *q, int x);

/* Dequeue the front element into *out (if non-NULL). Returns false if empty. */
bool   dequeue(Queue *q, int *out);

/* Read the current front element into *out (if non-NULL). Returns false if empty. */
bool   queue_front(const Queue *q, int *out);

#ifdef __cplusplus
}
#endif

#endif /* QUEUE_H */
