#include <stdio.h>
int main() {
    int a,b,c;
	scanf("%d %d %d",&a,&b,&c);
    while (c--)
        a ^= b;
	printf("%d",a);
}
