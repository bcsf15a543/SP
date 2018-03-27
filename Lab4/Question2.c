#include<stdio.h>
#include<stdlib.h>
int main()
{
   
    printf("sbrk(0) before 0x%x",sbrk(0));
    printf("\n");
    int *p1,*p2,*p3,*p4;
    p1=(int*)malloc(10);
    printf("After running: p1=(int*)malloc(10), sbrk(0) becomes 0x%x",sbrk(0));
    printf("\n");
    p2=(int*)malloc(2);
    printf("After running: p2=(int*)malloc(2), sbrk(0) becomes 0x%x",sbrk(0));
    printf("\n");
    p3=(int*)malloc(3);
    printf("After running: p3=(int*)malloc(3), sbrk(0) becomes 0x%x",sbrk(0));
    printf("\n");
    p4=(int*)malloc(1);
    printf("After running: p4=(int*)malloc(1), sbrk(0) becomes 0x%x",sbrk(0));
    printf("\n");
    printf("Value of p1 :  0x%x",p1);
    printf("\n");
    printf("Value of p2 :  0x%x",p2);
    printf("\n");
    printf("Value of p3 :  0x%x",p3);
    printf("\n");
    printf("Value of p4 :  0x%x",p4);
    printf("\n");

}
