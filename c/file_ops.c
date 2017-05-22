#include <stdio.h>

int main()
{
    FILE *fp = fopen("test.txt", "r");
    FILE *fp2 = fopen("test.txt", "r+");
    char string[256];
    
    while(fgets(string, sizeof(string), fp))
    {
        if(strstr(string, "vishwas"))
        {
            fputs("kavya\n", fp2);
            fputs(string, fp2);
            break;
        }
        fgets(string, sizeof(string), fp2);
    }

    fclose(fp2);
    fclose(fp);
}
