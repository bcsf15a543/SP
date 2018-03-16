#include<stdio.h>
int isEqual(int num1,int num2)
{

 if (num1==num2)
{
 return 1;
}
else
{
  return -1;
}

}
void Swap(int num1,int num2)
{
  num1=num1*num2;
  num2=num1/num2;
  num1=num1/num2;
  printf("Number 1 = %d",num1);
  printf("\n");
  printf("Number 2 = %d",num2);

}
