#include<stdlib.h>
#include<signal.h>
void sigint_handler(int signum){
signal(SIGINT,SIG_IGN);
}
void sigquit_handler(int signum){
signal(SIGQUIT,SIG_IGN);
}
void sigtstp_handler(int signum){
signal(SIGTSTP,SIG_IGN);
}
void sigfpe_handler(int signum){
signal(SIGFPE,SIG_IGN);
}
void sighup_handler(int signum){
signal(SIGHUP,SIG_IGN);
}
int main()
{
  printf("Ignoring signals...");
  signal(SIGINT,sigint_handler);
  signal(SIGFPE,sigfpe_handler);
  signal(SIGQUIT,sigquit_handler);
  signal(SIGHUP,sighup_handler);
  signal(SIGTSTP,sigtstp_handler);
  return 0;
 
 
}
