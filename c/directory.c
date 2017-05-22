#include <stdio.h>
#include <dirent.h>

int main()
{
    DIR *dir;
    struct dirent *d;
    int len;
    char cmd[256];

    dir = opendir("/users/vibhat/code/vishwas");    
    if (dir == NULL)
    {
        printf("This directory could not be opened.\n");
        return 1;
    }
    
    while(d = readdir(dir))
    {
        len = strlen(d->d_name);
        if(strcmp(".iso", &d->d_name[len-4]) == 0) 
        {
            printf("File found: %s, length: %d\n", d->d_name, len);
        }
    }

    closedir(dir);
    
    return 0;
}
