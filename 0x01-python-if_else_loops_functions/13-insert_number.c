#include "lists.h"
#include <stdlib.h>
#include <stddef.h>
/**
 * insert_node - function to insert note into linked list
 * @head: poiner to the first node of the linked list
 * @number: number to be inserted to the linked
 * Return: newly formatted linked list
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *new;
	
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	if (node == NULL || node->n >= number)
	{
		new ->next = node;
		*head = new;
		return (new);
	}
	while (node && node->next && node->next->n < number)
		node = node->next;
	new->next = node->next;
	node->next = new;

	return (new);
}
