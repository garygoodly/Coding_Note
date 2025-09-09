#include <stdio.h>
#include <stdlib.h>
#include "linkedlist.h"

struct ListNode* createNode(int val) {
    struct ListNode* newNode = (struct ListNode*)malloc(sizeof(struct ListNode));
    newNode->val = val;
    newNode->next = NULL;
    return newNode;
}

struct ListNode* array2linkedlist(int* arr, int size) {
    if (size == 0) return NULL;
    struct ListNode* head = createNode(arr[0]);
    struct ListNode* curr = head;
    for (int i = 1; i < size; i++) {
        curr->next = createNode(arr[i]);
        curr = curr->next;
    }
    return head;
}

void printlinkedlist(struct ListNode* head) {
    while (head != NULL) {
        printf("%d ", head->val);
        head = head->next;
    }
    printf("\n");
}

void freelinkedlist(struct ListNode* head) {
    struct ListNode* curr = head;
    while (curr != NULL) {
        struct ListNode* tmp = curr;
        curr = curr->next;
        free(tmp);
    }
}

// 203 - while
// struct ListNode* removeElements(struct ListNode* head, int val) {
//     struct ListNode* dummy = (struct ListNode*)malloc(sizeof(struct ListNode));
//     dummy->next = head;
//     struct ListNode* curr = dummy;
//     while (curr->next != NULL) {
//         if (curr->next->val == val) {
//             struct ListNode* tmp = curr->next;
//             curr->next = curr->next->next;
//             free(tmp);
//         } else {
//             curr = curr->next;
//         }
//     }
//     struct ListNode* newHead = dummy->next;
//     free(dummy);
//     return newHead;
// }

// 203 - recursive
/*
    **問題：**我要從一個鏈結串列中移除所有值為 val 的節點。
    **遞迴假設：**我假設 head->next 這條鏈已經處理好了（這是遞迴的核心）。
    **我該做什麼？**我只要處理 head 這個節點就好：
    如果 head->val == val，我就跳過它（刪掉它）。
    否則，我保留它，並把 head->next 指向處理後的結果。
*/
struct ListNode* removeElements(struct ListNode* head, int val) {
    if (head == NULL) return head;

    head->next = removeElements(head->next, val);
    if (head->val == val) {
        struct ListNode* tmp = head->next;
        free(head);
        return tmp;
    }
    else {
        return head;
    }
}

// 206 - recursive
struct ListNode* reverseList(struct ListNode* head) {
    if (head == NULL || head->next == NULL) return head;
    struct ListNode* newHead = reverseList(head->next);
    head->next->next = head;
    head->next = NULL;
    return newHead;
}

// 24
// struct ListNode* swapPairs(struct ListNode* head) {
//     if (head == NULL || head->next == NULL) return head;

//     struct ListNode* dummy = (struct ListNode*)malloc(sizeof(struct ListNode));
//     dummy->next = head;

//     struct ListNode* curr = dummy;
//     struct ListNode* tmp = curr->next;
//     while (tmp && tmp->next) {
//         curr->next = tmp->next;
//         curr = curr->next;
//         tmp->next = curr->next;
//         curr->next = tmp;
//         curr = tmp;
//         tmp = curr->next;
//     }
//     return dummy->next;
// }

// 24 - recursive
struct ListNode* swapPairs(struct ListNode* head) {
    if (head == NULL || head->next == NULL) return head;
    struct ListNode* tmp = head->next;
    head->next = swapPairs(tmp->next);
    tmp->next = head;
    return tmp;
}

// 19
struct ListNode* removeNthFromEnd(struct ListNode* head, int n) {
    struct ListNode* dummy = (struct ListNode*)malloc(sizeof(struct ListNode));
    dummy->next = head;
    struct ListNode* fast = dummy;    
    struct ListNode* slow = dummy;
    for (; n > 0; n--) 
        fast = fast->next;

    while (fast->next != NULL) {
        fast = fast->next;
        slow = slow->next;
    }
    struct ListNode* tmp = slow->next;
    slow->next = tmp->next;
    free(tmp);
    return dummy->next;
}

// 160
// struct ListNode *getIntersectionNode(struct ListNode *headA, struct ListNode *headB) {
//     int lenA = 0, lenB = 0;
//     struct ListNode *currA = headA, *currB = headB;
//     while (currA != NULL) {
//         lenA++;
//         currA = currA->next;
//     }
//     while (currB != NULL) {
//         lenB++;
//         currB = currB->next;
//     }
//     currA = headA;
//     currB = headB;
//     if (lenA > lenB)
//         for (int i = 0; i < lenA - lenB; i++)
//             currA = currA->next;
//     else 
//         for (int i = 0; i < lenB - lenA; i++)
//             currB = currB->next;
//     if (currA == currB) return currA;
//     while (currA->next != currB->next) {
//         currA = currA->next;
//         currB = currB->next;
//     }
//     return currA->next;
// }

// 160
struct ListNode *getIntersectionNode(struct ListNode *headA, struct ListNode *headB) {
    if (headA == NULL || headB == NULL) return NULL;
    struct ListNode *pA = headA, *pB = headB;
    while (pA != pB) {
        pA = pA ? pA->next : headB;
        pB = pB ? pB->next : headA;
    }
    return pA;
}

// 142
struct ListNode *detectCycle(struct ListNode *head) {
    struct ListNode *fast = head, *slow = head;
    while (fast != NULL && fast->next != NULL) {
        fast = fast->next->next;
        slow = slow->next;
        if (fast == slow) {
            slow = head;
            while (fast != slow) {
                fast = fast->next;
                slow = slow->next;
            }
            return fast;
        }
    }
    return NULL;
}