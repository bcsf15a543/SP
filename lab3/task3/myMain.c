
#include<stdio.h>
#include"myMath.h"
#include"myStr.h"
int main ()
{
        printf("Executing first task\n");
        int num1;
	int num2;;
	printf("Enter number 1 : ");
	scanf("%d",&num1);
	printf("\n");
	printf("Enter number 2 : ");
	scanf("%d",&num2);
	int is_equal_rst=isEqual(num1,num2);
	if(is_equal_rst == 1)
	{
	   printf("yes the two numbers %d,%d are equal",num1,num2);

	}
	else
	{
	  printf("no the two numbers are not equal");
	}
	printf("Before swapping ...\n");
	printf("Number 1 = %d : ",num1);
	printf("\n");
	printf("Number 2 = %d : ",num2);
	printf("After swapping ...\n");
	Swap(num1,num2);
        printf("\n");
   
        printf("Executing second task\n");
        int status=isPalindrome("abba",4);
	if (status == 1)
	{
	  printf("\nYes it a palindrome");
	}
	else
	{
	   printf("\nNo it is not a palindrome");
	}
	printf("\n");
	return 1;

}


