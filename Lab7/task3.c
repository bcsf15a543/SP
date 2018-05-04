#include<stdio.h>
#include<stdlib.h>
#include<fcntl.h>
void main()
{
 
	int n;
	char buff[256];
        int fd=open("abc.txt",O_CREAT|O_RDWR,0777);
	for(;;)
	{
	  n=read(0,buff,255);
	  if (n<=0)
	   {
	      break;
	   }
	  write(fd,buff,n);
	}

}
