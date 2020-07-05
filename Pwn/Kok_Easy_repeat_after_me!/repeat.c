#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>

int main(int argc, char **argv){

  setvbuf(stdout, NULL, _IONBF, 0);

  char buf[64];
  char flag[64];
  char *flag_ptr = flag;
  
  // Set the gid to the effective gid
  gid_t gid = getegid();
  setresgid(gid, gid, gid);

  memset(buf, 0, sizeof(flag));
  memset(buf, 0, sizeof(buf));

 
  
  
  FILE *file = fopen("flag.txt", "r");
  if (file == NULL) {
    printf("Flag File is Missing. Problem is Misconfigured, please contact an Admin if you are running this on the shell server.\n");
    exit(0);
  }
  
  // everything above this is for problem set-up and is irrelevant to your solving, this is the main "meat" of the program
  puts("ECHO AFTER ME YA! ECHO AFTER YOU AH! ECHO EVEN LOUDER! ECHO EVEN LOUDER!\n\nI, S9123456A RECRUIT BOBBY TAN WILL REPEAT EVERYTHING YOU SAY:\n\n");
  fgets(flag, sizeof(flag), file);
  
  while(1) {
    printf("> ");
    fgets(buf, sizeof(buf), stdin);
    printf(buf);
  }  
  return 0;
}
