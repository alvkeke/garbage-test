#include "wavfile.h"


LPFRAME createEmptyHead()
{
	LPFRAME node = (LPFRAME)malloc(sizeof(Frame));
	node->next = NULL;
	return node;
}

LPFRAME createListHead(int left, int right)
{
	return createNode(left, right);
}

LPFRAME createNode(int left, int right)
{
	LPFRAME node = (LPFRAME)malloc(sizeof(Frame));
	node->leftSample = left;
	node->rightSample = right;
	node->next = NULL;
	return node;
}

LPFRAME addWateNode(LPFRAME tail, LPFRAME node)
{
	if (!tail)
	{
		
	}

	tail->next = node;
	node->next = NULL;
	return node;
}

LPFRAME delWateNode(LPFRAME list, LPFRAME node)
{

}

int getNodeCount(LPFRAME list)
{
	LPFRAME it;
	int count = 0;
	for(it = list; it->next!=NULL; it = it->next)
	{
		count++;
	}
	return count;
}