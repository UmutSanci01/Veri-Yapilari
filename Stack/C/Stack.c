#include <stdlib.h>
#include <stdio.h>

#include "Stack.h"

struct Stack {
    unsigned int capacity;
    unsigned int size;
    int *datas;
};

struct Stack *stack_init(unsigned int capacity)
{
    struct Stack *s = (struct Stack *)malloc(sizeof(struct Stack));
    if (s == NULL)
    {
        fprintf(stderr, "Stack, Memory allocation failed\n");
        return NULL;
    }

    s->datas = (int *)malloc(capacity * sizeof(int));
    if (s->datas == NULL)
    {
        fprintf(stderr, "Stack/datas, Memory allocation failed\n");
        return NULL;
    }

    s->capacity = capacity;
    s->size = 0;

    return s;
}

void stack_push(struct Stack *stack, int data)
{
    if (stack->size >= stack->capacity)
    {
        stack->datas = (int *)realloc(stack->datas, stack->capacity * 2);
        if (stack->datas == NULL)
        {
            fprintf(stderr, "Stack, Memory resize failed\n");
            return;
        }
        stack->capacity *= 2;
    }

    stack->datas[stack->size++] = data;
}

int stack_pop(struct Stack *stack)
{
    if (stack->size == 0)
    {
        fprintf(stderr, "Stack, pop failed\n");
        return -1;
    }

    int data = stack->datas[--stack->size];
    return data;
}

void stack_free(struct Stack *stack)
{
    free(stack);
    stack = NULL;
}

// return capacity of stack
unsigned int stack_cap(struct Stack *stack)
{
    return stack->capacity;
}

// return current data amount of stack
unsigned int stack_size(struct Stack *stack)
{
    return stack->size;
}