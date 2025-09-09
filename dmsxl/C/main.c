#include <stdbool.h>


typedef struct {
    int in;
    int out;
    int sin[100];
    int sout[100];
} MyQueue;


MyQueue* myQueueCreate() {
    MyQueue* queue = (MyQueue* )malloc(sizeof(MyQueue));
    queue->in = 0;
    queue->out = 0;
    for (int i = 0; i < 100; i++)
        queue->sin[i] = queue->sout[i] = 0;
    return queue;
}

void myQueuePush(MyQueue* obj, int x) {
    obj->sin[obj->in++] = x;
}

int myQueuePop(MyQueue* obj) {
    if (obj->out > 0) 
        return obj->sout[--obj->out];
    while (obj->in)
        obj->sout[obj->out++] = obj->sin[--obj->in];
    return obj->sout[--obj->out];
}

int myQueuePeek(MyQueue* obj) {
    return obj->out ? obj->sout[obj->out - 1] : obj->sin[0];
}

bool myQueueEmpty(MyQueue* obj) {
    return !(obj->in * obj->out);    
}

void myQueueFree(MyQueue* obj) {
    obj->in = obj->out = 0;
}

/**
 * Your MyQueue struct will be instantiated and called as such:
 * MyQueue* obj = myQueueCreate();
 * myQueuePush(obj, x);
 
 * int param_2 = myQueuePop(obj);
 
 * int param_3 = myQueuePeek(obj);
 
 * bool param_4 = myQueueEmpty(obj);
 
 * myQueueFree(obj);
*/