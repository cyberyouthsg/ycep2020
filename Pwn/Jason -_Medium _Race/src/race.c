#include <stdio.h>
#include <errno.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>

int main(int argc, char* argv[])
{
        int fd;
        char buf[256];

        if(argc != 2)
        {
                fprintf(stderr, "usage: %s <filename>\n", argv[0]);
                exit(1);
        }


        if(!access(argv[1], R_OK))
        {
                fd = open(argv[1], O_RDONLY);

                if(fd <= 0)
                {
                        fprintf(stderr, "%s could not be opened\n", argv[1]);
                        exit(1);
                }

                write(1, buf, read(fd, buf, 256));
        }
        else
        {
                fprintf(stderr, "cat: %s: Permission denied\n", argv[1]);
        }
}