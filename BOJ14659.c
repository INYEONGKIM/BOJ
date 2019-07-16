#include<stdio.h>
int a[30000];
int main(){
	int n,g=0;
	scanf("%d",&n);
	for(int i=0; i<n; i++){
		scanf("%d",&a[i]);
	}
	for(int i=0; i<n; i++){
		int c=a[i];
		int t=0;
		for(int j=i+1; j<n; j++){
			if(c<a[j])
				break;
			else
				t++;
		}
		if(t>g) g=t;
	}
	printf("%d\n", g);
	return 0;
}
