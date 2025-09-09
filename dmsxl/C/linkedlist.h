#ifndef LINKEDLIST_H
#define LINKEDLIST_H

struct ListNode {
    int val;
    struct ListNode* next;
};

struct ListNode* createNode(int val);
struct ListNode* array2linkedlist(int* arr, int size);
void printlinkedlist(struct ListNode* head);
void freelinkedlist(struct ListNode* head);
struct ListNode* removeElements(struct ListNode* head, int val);
struct ListNode* reverseList(struct ListNode* head);
struct ListNode* swapPairs(struct ListNode* head);

#endif
