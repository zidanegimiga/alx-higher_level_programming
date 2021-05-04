#include <stdlib.h>
#include <stdio.h>
#include "lists.h"

/**
 * list_len - finds the number of elements in a linked list
 * @h: pointer to linked list
 *
 * Return: number of elements in linked list
 */
size_t list_len(listint_t *h)
{
	size_t nodes = 0;

	if (h == NULL)
		return (0);
	while (h != NULL)
	{
		nodes++;
		h = h->next;
	}
	return (nodes);
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: double pointer to head node of listint_t singly linked list
 *
 * Return: 1 if palindrome, 0 if not
 */
int is_palindrome(listint_t **head)
{
	int *nArr, start = 0, end = 0, len = 0;
	listint_t *temp;

	if (*head == NULL)
		return (1);
	temp = *head;
	len = list_len(temp);
	nArr = (int *)malloc(sizeof(int) * len);
	if (nArr == NULL)
		return (2);
	temp = *head;
	while (temp != NULL)
	{
		nArr[end] = temp->n;
		end++;
		temp = temp->next;
	}
	for (start = 0, end = len - 1; start < end; start++, end--)
	{
		if (nArr[start] != nArr[end])
			return (0);
	}
	return (1);
}
