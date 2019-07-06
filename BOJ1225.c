#include<stdio.h>
#include<string.h>
int main(){
    long long int sum=0;
    char arr[10005];
    char arr2[10005];
    scanf("%s %s", arr, arr2);
    for (int i = 0; i < strlen(arr); i++){
        for (int j = 0; j < strlen(arr2); j++){
            sum += ((arr[i]-'0')*(arr2[j]-'0'));
        }
    }
    printf("%lld", sum);
}
