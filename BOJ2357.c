#include <stdio.h>
#define MAX_N 100000
#define INF 1900000000

int n, m, maxseg[4 * MAX_N], minseg[4 * MAX_N], a, b;

int max(int x, int y){
    if (x>y)
        return x;
    return y;
}

int min(int x, int y){
    if (x<y)
        return x;
    return y;
}

int maxupdate(int pos, int val, int node, int x, int y){
    if (y < pos || pos < x)
        return maxseg[node];
    if (x == y)
        return maxseg[node] = val;
    int mid = (x + y) >> 1;
    return maxseg[node] = max(maxupdate(pos, val, node * 2, x, mid), maxupdate(pos, val, node * 2 + 1, mid + 1, y));
}

int maxquery(int lo, int hi, int node, int x, int y){
    if (y < lo || hi < x)
        return -INF;
    if (lo <= x&&y <= hi)
        return maxseg[node];
    int mid = (x + y) >> 1;
    return max(maxquery(lo, hi, node * 2, x, mid), maxquery(lo, hi, node * 2 + 1, mid + 1, y));
}

int minupdate(int pos, int val, int node, int x, int y){
    if (y < pos || pos < x)
        return minseg[node];
    if (x == y)
        return minseg[node] = val;
    int mid = (x + y) >> 1;
    return minseg[node] = min(minupdate(pos, val, node * 2, x, mid), minupdate(pos, val, node * 2 + 1, mid + 1, y));
}

int minquery(int lo, int hi, int node, int x, int y){
    if (y < lo || hi < x)
        return INF;
    if (lo <= x&&y <= hi)
        return minseg[node];
    int mid = (x + y) >> 1;
    return min(minquery(lo, hi, node * 2, x, mid), minquery(lo, hi, node * 2 + 1, mid + 1, y));
}

int main(){
    scanf("%d%d", &n, &m);
    for (int i = 1; i <= n; i++) {
        scanf("%d", &a);
        maxupdate(i, a, 1, 1, n);
        minupdate(i, a, 1, 1, n);
    }
    for (int i = 0; i < m; i++) {
        scanf("%d%d", &a, &b);
        printf("%d %d\n", minquery(a, b, 1, 1, n), maxquery(a, b, 1, 1, n));
    }
    return 0;
}
