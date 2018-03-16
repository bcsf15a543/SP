#include<stdio.h>
#include<myStr.h>
int main()
{

	char my_string[]="aba";
	int status=isPalindrome(my_string,3);
	if (status == 1)
	{
	  printf("Yes %s is a palindrome\n",my_string);
	}
	else
	{
	   printf("No %s is is not a palindrome\n",my_string);
	}
	return 1;

}
