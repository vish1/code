#include <stdio.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <unistd.h>

#define BKUP_LIMIT 100 

int get_backup_filename()
{   
    struct stat st;
    int i=0;
    char str[100], str2[10];
    
    for (i=0;i<BKUP_LIMIT;i++)
    {
        strcpy(str, "a.bak");
        if(i>0) 
        {
            sprintf(str2, "%d",i);
            strcat(str, str2);
        }
        if(stat(str ,&st) != 0)
            break;
    }
    if(i==BKUP_LIMIT)
    {
        return 1;
    }
    printf ("Backup filename is: %s", str);
    return 0;
}

int main()
{
    int rc=0;
    rc = get_backup_filename();
    if(rc == 1)
        printf("Error in get_backup_filename: "
                "backup limit reached");
    return 0;
}
