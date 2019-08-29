#include<stdio.h>
int main(){
	int k,n,m,c;
	scanf("%d",&k);
	while(k--){
		c=0;
		scanf("%d %d",&n,&m);
		for(int a=1; a<n; a++)
			for(int b=a+1; b<n; b++)
				if((a*a+b*b+m)%(a*b)==0) c++;
		printf("%d\n",c);	
	}
	return 0;
}
