#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>
void main()
{
   pid_t cpid;
   cpid=fork();
   int status=0;
   if(cpid==0)
   {
    exit(-1);
   } 
   else
   {
    wait(&status);
    if(WIFEXITED(status))
   {
    printf("Normal Termination , status=%d \n",WEXITSTATUS(status));
   }

   }
   
}
