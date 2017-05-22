#include <stdio.h>
#include <string.h>

void perm(char* orig, char* new, int* covered, int iter)
{   
    int i;
    if(strlen(orig)!=iter)
    {
        for(i=0;(i<strlen(orig));i++)
        {
            if(covered[i]==0)
            {    
                new[iter]=orig[i];
                covered[i]=1;
                perm(orig, new, covered, iter+1);
                covered[i]=0;
            }
        }
    }
    else printf("%s\n",new);
}

int main()
{
    char original[10],new[10]={'\0'};
    int covered[10]={0};
    scanf("%s",original);
    original[strlen(original)]='\0';
    perm(original, new, covered, 0);
    return 1;   
}

