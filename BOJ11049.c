#include <stdio.h>
#define min(a,b) ((a)<(b))?(a):(b)
#define INF 987654321
int N;
int dp[502][502];
int d[502];
int main(){
    scanf("%d", &N);
    scanf("%d%d", &d[0],&d[1]);
    for (int i = 1; i < N-1; i++)
        scanf("%d%d", &d[i],&d[i+1]);
    scanf("%d%d", &d[N-1], &d[N]);
    for (int dia=1; dia <= N; dia++){
        for (int i=1; i<=N-dia; i++){
            int j=i+dia;
            if (i==j){
                dp[i][j] = 0;
                continue;
            }
            dp[i][j] = INF;
            for (int k=i; k<j; k++){
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] + d[i-1]*d[k]*d[j]);
            }
        }
    }
    printf("%d\n", dp[1][N]);
    return 0;
}
