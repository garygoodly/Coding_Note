#include "queue.h"
#include <stdlib.h>

/* Compute the physical index corresponding to logical offset i from head. */
static inline size_t q_index(const Queue *q, size_t i) {
    return (q->head + i) % q->cap;
}

/* Grow underlying storage while preserving logical order [head .. head+size). */
static bool queue_grow(Queue *q) {
    size_t ncap = q->cap ? q->cap * 2 : 16;
    int *nd = (int*)malloc(sizeof(int) * ncap);
    if (!nd) return false;

    for (size_t i = 0; i < q->size; ++i)
        nd[i] = q->data[q_index(q, i)];

    free(q->data);
    q->data = nd;
    q->cap  = ncap;
    q->head = 0;   /* after relinearization, front is at index 0 */
    return true;
}

bool queue_init(Queue *q, size_t init_cap) {
    if (!q) return false;
    q->size = 0;
    q->head = 0;
    q->cap  = init_cap ? init_cap : 16;
    q->data = (int*)malloc(sizeof(int) * q->cap);
    return q->data != NULL;
}

void queue_free(Queue *q) {
    if (!q) return;
    free(q->data);
    q->data = NULL;
    q->size = 0;
    q->head = 0;
    q->cap  = 0;
}

bool queue_empty(const Queue *q) {
    return !q || q->size == 0;
}

size_t queue_size(const Queue *q) {
    return q ? q->size : 0;
}

bool enqueue(Queue *q, int x) {
    if (!q) return false;
    if (q->size == q->cap) {
        if (!queue_grow(q)) return false;
    }
    size_t tail = q_index(q, q->size); /* write at logical end */
    q->data[tail] = x;
    q->size++;
    return true;
}

bool dequeue(Queue *q, int *out) {
    if (!q || q->size == 0) return false;
    if (out) *out = q->data[q->head];
    q->head = (q->head + 1) % q->cap;
    q->size--;
    return true;
}

bool queue_front(const Queue *q, int *out) {
    if (!q || q->size == 0) return false;
    if (out) *out = q->data[q->head];
    return true;
}
