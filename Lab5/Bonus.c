#include<stdio.h>
#include<stdlib.h>
int mysystem(char *);
int main ()
{
   printf("Running ls command ...\n");
   mysystem("ls");
   printf("Done");
   exit(0);
}
int mysystem(char * cmd)
{
  int status;
 pid_t cpid;
 cpid=fork();
 switch(cpid)
{
 case -1:
 perror("Fork failed\n");
 return -1;
 case 0:
 execlp("/bin/bash","mybash","-c",cmd,'\0');
 _exit(127);
 default:
  waitpid(cpid,&status,0);
  return status;
}

}
