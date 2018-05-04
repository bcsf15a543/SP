#include<stdio.h>
#include<stdlib.h>
#include<fcntl.h>
void main(int argc ,char* argv[])
{
      
        // cat file 1>output
	// cat file 2>&1
	int n;  
	char buff[1024];
        int fd1=open("src.txt",O_RDONLY);
      	if (argc==2)
       	{
       		close(1);
	        int fd2=open(argv[1],O_CREAT|O_RDWR,0777);
       	}
	printf("Welcome \n");
/*	for(;;)
	{
	  n=read(fd1,buff,1023);
	  if (n<=0)
	   {
	      break;
	   }
          if(argv[1]!=NULL)
         {
          
           //stdout?

	  write(1,buff,n);
	 }
         else
         {
            printf("file error");
         }
	}
*/
}
