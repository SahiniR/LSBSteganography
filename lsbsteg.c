#include<stdio.h>
#include<stdlib.h>


typedef struct
{
    unsigned short type;
    unsigned int size;
    unsigned int reserve;
    unsigned int offset;
}HEADER;


typedef struct bitmap_header_info
{
    unsigned int header_size;
    int width;
    int height;
    unsigned short planes;
    unsigned short bits;
    unsigned int compression;
    unsigned int img_size;
    int xres;
    int yres;
    unsigned int ncolours;
    unsigned int impcolours;
}HEADERINFO;
typedef struct
{
    unsigned char r,g,b,j;
}PIXEL;

int main(){
unsigned short *test;
unsigned int *test1;

char string[100];
FILE *bmp;

bmp=fopen("testimage.bmp","rb");
HEADER h1;
HEADERINFO hi1;

fread(&h1,sizeof(HEADER),1,bmp);
if (h1.type !=0x4D42)
    {
        fclose(bmp);
        return 0;
    }
// fread(&hi1,sizeof(HEADERINFO),1,bmp);
// printf("width=%d",hi1.width);
//printf("%d",*test1);
//printf("%d",*test1);
// printf("please enter the string to be encoded");
// scanf("%s",string);
}