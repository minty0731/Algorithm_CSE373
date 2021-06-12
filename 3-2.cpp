/* problem: Write a program to reverse the direction
of a given singly-linked list. In other words, after
the reversal all pointers should now point backwards.
Your algorithm should take linear time */

typedef struct Node {
    char *value;
    struct Node *next;
} Node;

int reverse(Node **head) {
    Node *curr, *prev, *next;

    if (!head || !(*head)) {
        return 0;
    }

    curr = *head;
    prev = NULL;
    next = NULL;

    while (curr) {
        next =  curr->next;
        curr->next = prev;
        prev = curr;
        curr = next;
    }

    *head = prev;

    return 1;
}