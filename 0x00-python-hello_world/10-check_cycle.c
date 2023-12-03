#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - checks if a singly linked list
 * has a cycle in it.
 * @list: pointer
 * Return: 0 if there is no cycle, 1 if there is a cycle
*/

int check_cycle(listint_t *list)
{
	listint_t *slow_list = list, *fast_list = list;

	while (fast_list && fast_list->next)
	{
		slow_list = slow_list->next;
		fast_list = fast_list->next->next;
		if (slow_list == fast_list)
			return (1);
	}
	return (0);
}
