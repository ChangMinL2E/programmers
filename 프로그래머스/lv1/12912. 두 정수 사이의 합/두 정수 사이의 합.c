#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#define min(x, y) (x) < (y) ? (x) : (y) // x, y중에 작은값 반환
#define max(x, y) (x) > (y) ? (x) : (y) // x, y중에 큰값 반환


long long solution(int a, int b) {
    long long answer = 0;
    int minimum, maximum;
    minimum = min(a,b);
    maximum = max(a,b);
    
    for (minimum; minimum<=maximum; minimum++) {
        answer += minimum;
    }
    
    return answer;
}