#include<stdio.h>
#include"myMath.h"
int main()
{
int num1;
int num2;;
printf("Enter number 1 : ");
scanf("%d",&num1);
printf("Enter number 2 : ");
scanf("%d",&num2);
int is_equal_rst=isEqual(num1,num2);
if(is_equal_rst == 1)
{
   printf("\nyes the two numbers %d,%d are equal\n",num1,num2);

}
else
{
  printf("\nno the two numbers are not equal\n");
}
printf("\nBefore swapping ...\n");
printf("Number 1 = %d \n",num1);
printf("Number 2 = %d \n",num2);
printf("\nAfter swapping ...\n");
Swap(&num1,&num2);
printf("Number 1 = %d \n",num1);
printf("Number 2 = %d \n",num2);

return 0;
}
