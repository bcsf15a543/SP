#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>
void main()
{
   pid_t cpid;
   cpid=fork();
   if(cpid==-1)
   {
    printf("fork failed");
   }
   if(cpid==0)
   {
    printf("Child PID=%d \n",(long)getpid());
    printf("Child PPID=%d \n",(long)getppid());
  //  exit(1);
    } 
   else
   {
    wait(NULL);
    printf("Parent PID=%d \n",(long)getpid());
    printf("Parent PPID=%d \n",(long)getppid());
   }
}
