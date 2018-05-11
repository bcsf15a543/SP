#include<fcntl.h>
void main()
{
int fd1=open("f2",O_RDWR,0777);
dup2(fd1,0);
dup (1,2);
int fd2=open("f2",O_RDWR,0777);
dup2(fd2,1);
char buff [1024];
     int n;
     for (;;)
     {
	n=read(0,buff,1023);
	if (n<=0)
	{
         
	  return ;
	}
	write(1,buff,n);
        return;
     


}
    
}
