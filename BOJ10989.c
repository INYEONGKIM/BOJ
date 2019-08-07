#include<stdio.h>

int main(){
	int a[100001]={0,};
	int n,t,m=-1;
	scanf("%d",&n);
	for(int i=0; i<n; i++){
		scanf("%d",&t);
		a[t]++;
		if (m<t)
			m=t;
	}
	for(int i=1; i<=m; i++){
		if(a[i]!=0)
			for(int j=0; j<a[i]; j++)
				printf("%d\n",i);
	}
	return 0;
}
