#include <stdio.h>
#define LEN_INPUT 11

int main(void) {
    char s1[LEN_INPUT];
    scanf("%s", s1);
    int length, i;
    length = strlen(s1);
    for (i = 0; i < length; i = i+1) {
        printf("%c\n",s1[i]);
    }
    return 0;
}
