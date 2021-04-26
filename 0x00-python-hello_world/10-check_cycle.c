#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: pointer to the linked list
 * Return: Returns 0 to indicate no cycle  and 1 to indicate cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *temp = list;
	listint_t *temp2 = list;

	if (!list)
		return (0);

	while (temp && temp2 && temp2->next)
	{
		temp = temp->next;
		temp2 = temp2->next->next;

		if (temp == temp2)
			return (1);
	}
	return (0);


}
