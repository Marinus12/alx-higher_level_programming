#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
  * insert_node - Inserts a number into a sorted singly linked list.
  * @head: a pointer to the head of the list
  * @num: the number to insert
  *
  * Return: if function fails - NULL,
            a ponter to the new node otherwise
  */
listint_t *insert_node(listint_t **head, int num)
{
        listint_t *node = *head, *new;

        new = malloc(sizeof(listint_t));
        if (new == NULL)
                return (NULL);
        new->n = num;
        if (node == NULL || node->n >= num)
        {
                new->next = node;
                *head = new;
                return (new);
        }
        while (node && node->next && node->next->n < num)
                node = node->next;
        new->next = node->next;
        node->next = new;
        return (new);
}

