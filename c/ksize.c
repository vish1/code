#include <stdio.h>
#include <stdlib.h>


int main(int argc, char * argv[])
{
    int size, pow2=1;
    if (argc == 2)
    {
        size = atoi(argv[1]);
    }
    else
    {
        printf("Please enter a size value\n");
        return 1;
    }
    

    while(size > pow2)
        pow2 = pow2<<1;
   
    if((pow2 == 256) && (size < 192))
        pow2=192;
    if((pow2 == 128) && (size < 96))
        pow2=96;
        
    
    printf("%d\n", pow2 );
}
