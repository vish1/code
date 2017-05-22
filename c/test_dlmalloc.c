#include "stdio.h"

int main()
{
    int *i;
    i = (int *) malloc(sizeof(int)*20);
    i[0] = 25;

    printf("Printed value: %d\n", i[0]);

    free(i);   
    return 0;
}
