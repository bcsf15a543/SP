#include<stdio.h>
#include<unistd.h>
void main()
{
 uid_t ruid,euid,suid;
 gid_t rgid,egid,sgid;
 getresuid(&ruid,&euid,&suid);
 printf("Real user id before %d\n",(long)ruid);
 printf("Effective user id before %d\n",(long)euid);
 printf("Saved user id before %d\n",(long)suid);
 printf("\n\n");
 printf("After running : setuid(501)\n\n");
 int rv=setuid(501);
 if(rv==-1)
	{
	 getresuid(&ruid,&euid,&suid);
	 printf("Real user id after %d\n",(long)ruid);
	 printf("Effective user id after %d\n",(long)euid);
	 printf("Saved user id after %d\n\n",(long)suid);
	 
	}
  else
	{
	printf("Error occured \n");
	}
 

}
