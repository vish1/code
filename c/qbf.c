#include <stdio.h>
#include <string.h>

char *getMissingLetters(const char *sentence)
{
    char alphabet[26], temp;
    int len = strlen(sentence);
    int i, j, count=0;
    char *retvar= (char *)malloc(27 * sizeof(char));
   
    for(i=0;i<26;i++)
	alphabet[i]=0;
   
    for(i=0;i<len;i++)
    {
	temp = sentence[i];
	if((temp>64) && (temp<91))
	    alphabet[temp-65]=1;
	else if ((temp>96) && (temp<123))
	    alphabet[temp-97]=1;
    }

    j=0;
    for(i=0;i<26;i++)
    {
	if(alphabet[i]==0)
	{
	    retvar[j]= i+97;
	    j++;
	}
    }
    retvar[j]='\0';

    return retvar;
    
}

int main()
{
    char input_string[100];
    char *return_value;

    gets(input_string);

    return_value = getMissingLetters(input_string);
    printf("%s\n", return_value);

    free(return_value);
}
