#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void backup_file_name(char backup_name[])
{
   char* command1 = "ls -mr1 ";    char* back_file =  "a.bak";
char* command2 = "result.txt";
   char* extension =  ".bak";    char* command;
   FILE *fp;

//Chk if any back up file is present if not return immedaitely
   fp = fopen(back_file,"r");

  if(( fp!= NULL))
  {
      fclose(fp);
      command =(char*) malloc(100*sizeof(char));    command =
strcat(command, command1);    command = strcat(command, " ");
      command = strcat(command , back_file);    command =
strcat(command , "*");
      command = strcat(command , " > ");    command = strcat(command
, command2);
      system(command);
      fp = fopen("result.txt","rb+");
      char * line = NULL;    size_t len = 0;    ssize_t read;
      read = getline(&line, &len, fp);
      char *tp  = strstr(line , extension);
      char* t = tp + strlen(extension);
      sprintf(backup_name,"%s%d" , back_file,atoi(t) + 1 );

      //clean up
      //close the file
      fclose(fp);

      command[0]='\0'; //free the command buffer
      //This may prevent you from deleting as user executing program may not be a super user so dafe use  chmod before using it

      command = strcpy(command , "unlink");
      command = strcpy(command , "  ");
      command = strcpy(command , command2);
      system(command);
      free(command);


  }
  else
      sprintf(backup_name,"%s" , back_file);

}

int main()
{
   char p[100];
   backup_file_name(p);
   printf("Back up file name is %s" , p);
}

