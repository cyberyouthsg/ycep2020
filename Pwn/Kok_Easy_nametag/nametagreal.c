#include <stdio.h>
#include <stdlib.h>
int main()
{
    printf("Welcome to the nametag generator! What is your name?\n");
    
	char secret='b';
	char canary='x';
        char name[45];
	gets(name);
	printf("\n\nProcessing... we store our data in an internal addressbook while our minions go to work! How modern, right?\n\n");
	printf("canary: %p\n",(void *)&canary);
	printf("secret: %p\n",(void *)&secret);
	printf("name: %p\n\n",(void *)name);
	
	printf("Ok processing done! Here is a nametag with your name on it: [%s]\n", name);
        
	if(canary=='x' && secret=='a'){
		printf("YCEP{tweetytweet}");
	}
}
