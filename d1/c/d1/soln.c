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
            
            size_t ll = sizeof(line) / sizeof(line[0]);
            printf("size %d",ll);
            for(int i=0;line[i] != '\0'; i++){
                char cc = line[i];
                if (!isspace((unsigned char) cc)) {
                    if(isdigit((unsigned char) cc)){
                       printf("%c \n ",cc);
                       if(inc == 0){
                            c[0] = cc;
                            inc++;
                            
                            
                            
                            char last = line[ ll-1 ];
                            while(isspace((unsigned char) last)){
                               last--; 
                            }
                            line=line[last]+"\0"
                            printf("last: %c\n",last);
                            if(isdigit((unsigned char) last)){
                                c[1] = last;
                                continue;
                                }
                       }
                       else{
                        c[1]=cc;
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
