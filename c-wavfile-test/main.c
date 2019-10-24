#include "main.h"
#include "wavfile.h"

#define FILENAME "/home/alvis/desktop/wav-file-test/wav/output.wav"

int main()
{
	
	FILE *fp;
	fp = fopen(FILENAME, "rb");
	if(!fp) return 1;

	WavFile wav;
	fread(&wav, sizeof(WavFile), 1, fp);

	LPFRAME list = (LPFRAME)malloc(sizeof(Frame));
	LPFRAME tail = list;

	char samplelen = wav.BitsPerSample/8;
	int i = 0;
	tail->leftSample = 0;
	while(fread(&tail->leftSample, samplelen, 1, fp))
	{
		// fread(&tail->rightSample, samplelen, 1, fp);
		// printf("%d:\t%6x, %6x\n", i++, tail->leftSample, tail->rightSample);
		// tail->leftSample &= 0x00FF;

		adjustNum(&tail->leftSample, samplelen);

		printf("%d:\t%4.4x\n", i++, tail->leftSample);
		if (i == 48)
			continue;
		
		tail->next = (LPFRAME)malloc(sizeof(Frame));
		tail = tail->next;
		tail->next = NULL;
		tail->leftSample = 0;
	}
	
	printf("format: %d\n", wav.AudioFormat);
	printf("sample count = %d\n", getNodeCount(list));

	float time = wav.sub2Size / wav.ByteRate;
	printf("time = %f\n", time);

	fclose(fp);
	return 0;
}