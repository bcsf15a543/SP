#include<stdlib.h>
#include<signal.h>
int main()
{
	pid_t cpid = fork();
	if (cpid ==0){
	for(;;)
        {
	printf("Inside Child\n");
	sleep(2);
	}
}
else{
	printf("Inside Parent\n");
        sleep(3);
	kill(cpid,SIGINT);
	printf("I have terminated my child.. \n");
	exit(0);
    }
}
