#include<stdio.h>
#include<stdlib.h>
#include<setjmp.h>


int counter=0;
static jmp_buf envbuf;

void haveFun()
{
  printf("Calling haveFun()\n Value of counter is %d \n",counter);
  counter++;
 
}

void firstSetJump()
{

  printf("Calling firstSetJump()\n Value of counter is %d \n",counter);
  counter++;
  
}

int main()
{
   int x=0;
   for(;x<4;x++)
	{
	   if((setjmp(envbuf)==0) && counter==0)
	   {
	       firstSetJump();
	   }
           else
	   {
	       haveFun();
	   }
	}
return 0;
}
