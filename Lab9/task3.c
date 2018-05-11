#include<fcntl.h>
void main()
{
char buff [1024];
int fd=open("f1",O_RDWR,0777);//3
if (fd<=0)
{
	return;
}
else
{
      
     dup2(fd,1);//1->3
     
     dup2(1,2);
     
     dup2(1,0);//0->1
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
    
}
