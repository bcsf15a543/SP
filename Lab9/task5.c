#include<fcntl.h>
#include<stdlib.h>
#include<stdio.h>
#include<unistd.h>
void main(int argc,char *argv[])
{

if(argc!=2)
{
printf("Incorrect arguments");
return;
}

int i;
for(i=1;i<argc;i++)
{
  if(access(argv[i],R_OK)>-1)
 {
   printf("Read permission\n");
 }
 else
 {
   printf(" No Read permission\n");
 }
 if(access(argv[i],W_OK)>-1)
 {
   printf("Write permission\n");
 }
 else
 {
   printf(" No Write permission\n");
 }
 if(access(argv[i],X_OK)>-1)
 {
   printf("Execute permission\n");
 }
 else
 {
   printf(" No Execute permission\n");
 }


}


}
