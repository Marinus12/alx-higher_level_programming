#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
  * check_cycle - checks if a singly linked list contains a cycle
  * @li: singly linked list
  *
  * Return: if no cycle 0, if cycle 1
  */
int check_cycle(listint_t *li)
{
	listint_t *slow, *sped;

	if (li == NULL || li->next == NULL)
		return (0);
	slow = li->next;
	sped = li->next->next;

	while (slow && sped && sped->next)
	{
		if ( slow == sped)
			return (1);
		slow = slow->next;
		sped = sped->next->next;
	}
	return (0);
}
