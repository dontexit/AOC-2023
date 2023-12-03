#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>
struct AMap{
    const char *key;
    int value;
};

int main(){
    struct AMap m[] = {
        {"one",1},
        {"two",2},
        {"three",3},
        {"four",4},
        {"five",5},
        {"six",6},
        {"seven",7},
        {"eight",8},
        {"nine",9},
    };
    
    size_t ms = sizeof(m) / sizeof(m[0]);

    FILE *file;
    char *line = NULL;
    size_t len=0;
    char c[3];
    int cinc=0;
    int ccount=0;
    
    file = fopen("input1.txt","r");
    if(file == NULL){
        perror("Error opening file");
        return 1;
    }
    while (getline(&line,&len,file) != -1){
        size_t ll = sizeof(line) / sizeof(line[0]);
        printf("%s",line);
       c[0]='\0';
       c[1]='\0';
       ccount = 0;
       cinc=0;
       for (int i=0;i<ll;i++){
            char cc = line[i];
            if(!isspace((unsigned char) cc)){
                if(isdigit((unsigned char) cc)){
                    // if(inc == 0){
                    //     c[0] = cc;
                    //     cinc++;
                    // }
                    // else{
                    //     if(isdigit((unsigned char) line[cc-1])){
                    //      c[1] = line[cc-1];
                    //      continue;
                    //     } 
                    //     c[1]=cc;
                    }
                    printf("%c \n",cc);
                if(isalpha((unsigned char) cc)){
                    for(size_t j=0;j<ms;j++){
                        // printf("%s \n cc: %c \n",m[j].key,cc);
                        // sizeof ks = sizeof(m[j].key) / sizeof(m[j].key[0])
                        // for(int k;k<ks;k++){
                        //     printf("%s \n",m[j].key[k])
                        // }
                    }
                }
                }
                
            }
        }


  
    // for (size_t i = 0;i < ms;i++){
    //     printf("%d\n",m[i].value);
    // }
    fclose(file);
    free(line);
    return 0;
}
       

