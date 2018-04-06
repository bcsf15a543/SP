#include<stdio.h>
#include<unistd.h>
void main()
{
 uid_t ruid,euid;
 gid_t rgid,egid;
 getresuid(&ruid,&euid);
 printf("Real user id %d\n",(long)ruid);
 printf("Effective user id %d\n",(long)euid);
 getresgid(&rgid,&egid);
 printf("Real group id %d\n",(long)rgid);
 printf("Effective group id %d\n",(long)egid);
}
