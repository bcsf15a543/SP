#include<fcntl.h>
#include<stdlib.h>
#include<stdio.h>
#include<sys/stat.h>
#include<unistd.h>
void main(int argc,char *argv[])
{
 


int i;
for (i=1;i<argc;i++)
{
struct stat buf;
stat(argv[i],&buf);


if(S_ISREG(buf.st_mode))
{
 printf("%s is a file  \n", argv[i]);
 printf("UID : %d \n " ,buf.st_uid);
printf("Inode : %d \n" ,buf.st_ino);
 printf("Access time : %d \n",buf.st_atime);
 printf("Modify time : %d \n",buf.st_mtime);
 printf("Size : %d \n",buf.st_size);
 
 
}
else if(S_ISDIR(buf.st_mode))
{

 printf("%s is a directory \n", argv[i]);
 printf("UID : %d \n" ,buf.st_uid);
printf("Inode : %d \n" ,buf.st_ino);
 printf("Access time : %d \n",buf.st_atime);
 printf("Modify time : %d \n",buf.st_mtime);
 
 printf("Size : %d \n",buf.st_size);
}
}

}
