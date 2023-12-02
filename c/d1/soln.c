#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
int main(void){
       FILE *file;
       char *line = NULL;
        size_t len = 0;
        char c[3];
        int inc = 0; 
        int sum = 0;
       file = fopen("input.txt","r");
       if (file == NULL){
            perror("Error opening file");
            return 1;
       }
        
       while(getline(&line,&len,file) !=-1){
                        printf("%s",line);
            c[0]='\0';
            c[1]='\0';

            for(int i=0;line[i] != '\0'; i++){
                if (!isspace((unsigned char)line[i])) {
                    if(isdigit((unsigned char) line[i])){
                       printf("%c \n ",line[i]);
                       if(inc == 0){
                            c[0] = line[i];
                            inc++;
                       }
                       else{
                        c[1]=line[i];
                       }
                    }
                // printf("%c\n",line[i]);
            }
            }
                 if(inc==0){
                    c[0]='0';
                    c[1]='0';
                 }
                 else{
                    if(!isdigit((unsigned char) c[1])){
                        c[1]=c[0];
                    }
                 }
                 sum += atoi(c);
                printf("%c%c %d\n",c[0],c[1],sum);
                inc=0;
                                
       }
       fclose(file);
       free(line);
        return 0;

    }
