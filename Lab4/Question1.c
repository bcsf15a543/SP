#include<stdio.h>
#include<stdlib.h>
int main()
{
  int size=10;
  int * arr=(int*)malloc(sizeof(int)*size);
  int i;
  for(i=0;i<size;i++)
	{ 
	   arr[i]=i;
	}
  for(i=0;i<size;i++)
	{
	   printf("%d ",arr[i]);
	}
  printf("\n");
  int newsize=20;
  int * newarr=(int*)realloc(arr,sizeof(int)*newsize);
  arr=newarr;
    for(i=0;i<newsize;i++)
	{ 
	   newarr[i]=i;
	}
    for(i=0;i<newsize;i++)
	{
	   printf("%d ",newarr[i]);
	}
  printf("\n");
  free(arr);
  

}
