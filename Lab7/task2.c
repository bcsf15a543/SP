#include<stdio.h>
#include<stdlib.h>
#include<fcntl.h>
void main(int argc ,char* argv[])
{
      
	int n;
	char buff[1024];
        int fd1=open("/etc/passwd",O_RDONLY);
        int fd2=open(argv[1],O_CREAT|O_RDWR,0777);
	for(;;)
	{
	  n=read(fd1,buff,1023);
	  if (n<=0)
	   {
	      break;
	   }
	  write(fd2,buff,n);
	}

}
