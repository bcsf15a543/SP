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
 printf("After running : setresuid(1000,2000,300)\n\n");
 int rv=setresuid(1000,2000,300);
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
 printf("After running : setreguid(1000,2000,300)\n\n");
 int rv2=(setresgid(405));
 if(rv==-1)
       {
         getresgid(&rgid,&egid,&sgid);
	 printf("Real group id after %d\n",(long)rgid);
	 printf("Effective group id after %d\n",(long)egid);
	 printf("Saved group id after %d\n",(long)sgid);
        }
else
        {
	printf("Error occured \n");
        }

}
