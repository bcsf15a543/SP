#include<stdlib.h>
#include<signal.h>
int main()
{

  	sigset_t newset, oldset;
	sigemptyset(&newset);
	sigaddset(&newset, SIGINT);
	sigprocmask(SIG_SETMASK, &newset, &oldset);
	int i = 0;
	for(i=1; i<=5; i++)
        { 
        printf("Currently blocking sigint\n");
	sleep(2);
	}
	printf("Overwritng newmask with oldmask\n");
	sigprocmask(SIG_SETMASK, &oldset, NULL);
	for(i=1; i<=5; i++)
       {
	sleep(2);
       }
 return 0;
}
