/* strtok example */
#include <stdio.h>
#include <string.h>

int main ()
{
    char str[] ="10.7.1.4.6";
    char * pch;
    printf ("Splitting string \"%s\" into tokens:\n",str);
    pch = strtok (str,".");
    int i=0;
    while (pch != NULL)
    {
        i++;
        printf ("%s\n",pch);
        pch = strtok (NULL, ".");
    }
    printf("Count: %d\n",i);
    return 0;
}
