#include <stdio.h>

int main()
{
    int *i = (int *) malloc (sizeof(int));
    printf ("\nThe integer: %d\n", *i);
    return 0;
}
