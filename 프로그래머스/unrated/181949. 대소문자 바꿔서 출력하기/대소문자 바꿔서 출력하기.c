#include <stdio.h>
#define LEN_INPUT 10

int main(void) {
    char s1[LEN_INPUT];
    int i;
    scanf("%s", s1);
    // printf("%d",strlen(s1));
    
    for (i=0; i<strlen(s1); i++) {
        // printf("%d\n",s1[i]);
        if (s1[i] >= 97) {
            s1[i] -= 32;
        } else {
            s1[i] += 32;
        }
    }
    printf("%s", s1);
    return 0;
}
