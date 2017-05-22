void reverse_string(char **string_)
{
    char temp = '\0';
    char *string = *string_;
                            
    int len = strlen(string);
    int i, j;
                                    
    for(i = 0, j = len-1; i < j; i++, j--) {
        temp = string[i];
        string[i]= string[j];
        string[j]=temp;
    }

    return;
}
 
int main()
{
            char string[] = "he is me";
            reverse_string(&string);
            printf("The reverse is [%s]\n", string);
            return 0;
}
