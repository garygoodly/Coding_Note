#include <stdio.h>
#include "linkedlist.h"

int main() {
    int values[] = {1, 2, 3, 6, 5, 4, 6, 4, 6};
    int size = sizeof(values) / sizeof(values[0]);

    struct ListNode* head = array2linkedlist(values, size);
    printlinkedlist(head);

    head = removeElements(head, 6);
    printlinkedlist(head);

    freelinkedlist(head);
    return 0;
}
