#include<stdlib.h>
int isPalindrome (char *arr,int size)
{

   int flag=0;
   int i;
   char *r_s= malloc(4*1);
   int y=0;
   for (i=size-1;i>=0;i--)
   {
      r_s[y]=(int)arr[i];
      y=y+1;
   }

   for ( i=0;i<size;i++)
   {
     if ( arr[i] != r_s[i])
     { 
       flag=1;
       break;
     }
   }
 
  if (flag==1)
  {
   return -1;
  }
  
  else
  {
    return 1;
  }
  


}
