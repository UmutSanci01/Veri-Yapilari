#ifndef STACK_H
#define STACK_H

// C Encapsulation https://nerdyelectronics.com/encapsulation-information-hiding-c/

struct Stack *stack_init(unsigned int capacity);
void stack_push(struct Stack *stack, int data);
int stack_pop(struct Stack *stack);
void stack_free(struct Stack *stack);
unsigned int stack_cap(struct Stack *stack);
unsigned int stack_size(struct Stack *stack);

#endif