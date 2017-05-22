#include <stdio.h>

#define print_wrapper(args...) {printf(args);}

int main()
{
    print_wrapper("%s, \"%s\", %d\n", __FUNCTION__, "test", 5);
}
