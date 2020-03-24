#include <stdio.h>
int main(int argc, char const *argv[]) {
	int n;
	int dp[100001] = {0, };
	scanf("%d", &n);
	for(int i=1; i<=n; i++){
		dp[i] = i;
		for(int j=2; j*j<=i; j++){
			if (dp[i] > dp[i-j*j]+1){
				dp[i] = dp[i-j*j]+1;
			}
		}
	}
	printf("%d", dp[n]);
	return 0;
}
