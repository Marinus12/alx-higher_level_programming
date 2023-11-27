#ifndef LISTS_H
#define LISTS_H

/**
  * struct listint_s - singly linked list
  * @in: integer
  * @next: prints to the next node
  *
  * Description: singly linked list node structure
  *
  */
typedef struct listint_s
{
	int in;
	struct listint_s *next;
}listint_t;
size_t print_listint(const listint_t *h);
void free_listint(listint_t **head);
int check_cycle(listint_t *list);

#endif
