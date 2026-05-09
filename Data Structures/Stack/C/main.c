#include <stdio.h>
#include <stdlib.h>

#include "Stack.h"

int main(int argc, char **argv)
{
    struct Stack *s = stack_init(4);

    int n = 5;
    int arr[] = {3, 5, 1, 3, 6};
    for (int i = 0; i < n; i++)
    {
        stack_push(s, arr[i]);
        printf("stack capacity %u\n", stack_cap(s));
        // printf("stack size %u pop data %d\n", stack_size(s), stack_pop(s));
    }
    // printf("%d\n", stack_pop(s));

    stack_free(s);

    return 0;
}