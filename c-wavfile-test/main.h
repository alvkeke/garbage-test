#include "stdio.h"
#include "stdlib.h"

void adjustNum(int *num, short sampleLen)
{
	int x, orNum;
	switch (sampleLen)
	{
		case 1:
			x = 0x80;
			orNum = 0xFFFFFF00;
			break;
		case 2:
			x = 0x8000;
			orNum = 0xFFFF0000;
			break;
		case 3:
			x = 0x800000;
			orNum = 0xFF000000;
			break;
		default:
			return;
	}
	
	if(*num & x)
	{
		*num = *num | orNum;
	}
}