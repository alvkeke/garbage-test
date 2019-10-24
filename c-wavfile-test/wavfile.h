#include <stdio.h>

typedef struct Frame
{
	int leftSample;
	int rightSample;
	
	struct Frame* next;
}Frame;

typedef struct WavFile
{
	char ChunkId[4];
	unsigned int ChunkSize;
	char FileFormat[4];

	char sub1Id[4];
	unsigned int sub1Size;
	unsigned short AudioFormat;
	unsigned short NumChannels;
	unsigned int SimpleRate;
	unsigned int ByteRate;
	unsigned short BlockAlign;
	unsigned short BitsPerSample;

	char sub2[4];
	unsigned int sub2Size;

}WavFile;

typedef WavFile* LPWAVFILE;
typedef Frame* LPFRAME;

LPFRAME createEmptyHead();
LPFRAME createListHead(int left, int right);
LPFRAME createNode(int left, int right);
LPFRAME addWateNode(LPFRAME tail, LPFRAME node);
LPFRAME delWateNode(LPFRAME list, LPFRAME node);

int getNodeCount(LPFRAME list);