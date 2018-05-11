#include<fcntl.h>
void main()
{
char buff [1024];
int fd=open("errorAndoutput",O_RDWR,0777);//3
int fd2=dup(fd);//4
int fd3=open("newfile",O_RDONLY);//5
if (fd3<=0)
{
	close(2);
        dup2(fd,2);
	perror("error found");
	return;
}
else{
        int n;
	for (;;)
	{
	n=read(fd2,buff,1023);
	if (n<=0)
	{
         
	  return ;
	}
	write(fd2,buff,n);
        return;
	}

}
    
}
