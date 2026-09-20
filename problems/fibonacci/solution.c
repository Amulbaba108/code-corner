#include <stdio.h>

int main(void) {
    int n;
    scanf("%d", &n);
    int a = 0, b = 1;
    for (int i = 0; i < n; i++) {
        int next = a + b;
        a = b;
        b = next;
    }
    printf("%d\n", a);
    return 0;
}
