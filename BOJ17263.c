#include <stdio.h>
int main(){
	int n,t,m=-1;
	scanf("%d",&n);
	for(int i=0; i<n; i++){
		scanf("%d",&t);
		if (t>m){
			m=t;
		}
	}
	printf("%d",m);
	return 0;
}
