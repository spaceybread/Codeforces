#include <stdio.h>

int main() {
    
    int a;
    
    scanf("%d", &a); 

    if (a % 2 == 0) {
        if (a > 3) {
            printf("YES");
        }
        else {
            printf("NO");
        }
    }
    else {
        printf("NO");
    }

}
