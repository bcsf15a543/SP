#include<stdio.h>
#include<stdlib.h>
#include<fcntl.h>
void main(int argc ,char* argv[])
{
      
	int n;
	char buff[1024];
        int scr=open(argv[1],O_CREAT|O_RDWR,0777);
        if(scr==-1)
        {
           printf("error , no file exists");
           exit(1);
        }
        int des=open(argv[2],O_CREAT|O_RDWR,0777);
	for(;;)
	{
	  n=read(scr,buff,1023);
	  if (n<=0)
	   {
	      break;
	   }
	  write(des,buff,n);
	}
        
     unlink(argv[1]);

}
