#include<stdlib.h>
#include<signal.h>
void mySignalHandler(int signum)
{

	switch(signum){
	case 2: 
	printf("\nI got SIGINT: %d\n\n",signum);
	break;
	case 3:
	printf("\nI got SIGQUIT: %d\n\n",signum);
	break;
	case 20:
	printf("\nI got SIGTSTP: %d\n\n",signum);
	break;
	case 8:
	printf("\nI got SIGFPE: %d\n\n",signum);
	break;
	case 9:
	printf("\nI got SIGKILL: %d\n\n",signum);
	break;
        case 19:
	printf("\nI got SIGSTP: %d\n\n",signum);
	break;
        }
}
	
int main()
{
  printf("Registering handlers ...");
  signal(SIGINT,mySignalHandler);
  signal(SIGFPE,mySignalHandler);
  signal(SIGQUIT,mySignalHandler);
  signal(SIGHUP,mySignalHandler);
  signal(SIGTSTP,mySignalHandler);
  while(1)
  {
    printf("Insider loop...\n");
    sleep(2);
  }
  return 0;
 
 
}
