#include <stdio.h>

int main()
{
    struct bit_fields{
        int test:1,
            test2:1,
            test3:1,
            pad:14;
    } bf1, *bf2;
    
    int t = 0;
    bf1.test3 = 0;

    bf2 = &bf1;
    
    t = bf2->test3;

    if(t)
        printf("Bitfield test2 = %d\n", t);

    return 0;
}

