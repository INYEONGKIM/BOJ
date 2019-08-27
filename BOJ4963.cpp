#include<cstdio>
#include<iostream>
#include<queue>

int a[51][51];
int w,h,c;
int dx[8]={0,0,1,-1,1,-1,1,-1};
int dy[8]={1,-1,0,0,1,1,-1,-1};

using namespace std;

void bfs(int i, int j){
	int x,y;
	queue<int> q;
	a[i][j]=0;
	q.push(i);q.push(j);
	while(!q.empty()){
		x=q.front();q.pop();
		y=q.front();q.pop();
		a[x][y]=0;
		for(int z=0; z<8; z++){
			if(0<=x+dx[z] && x+dx[z]<h && 0<=y+dy[z] && y+dy[z]<w && a[x+dx[z]][y+dy[z]]==1){
				a[x+dx[z]][y+dy[z]]=0;
				q.push(x+dx[z]);q.push(y+dy[z]);
			}
		}
	}
}

int main(void){		
	while(1){
		c=0;
		scanf("%d %d",&w,&h);
		if (w==0 && h==0)
			break;
		for(int i=0; i<h; i++){
			for(int j=0; j<w; j++){
				scanf("%d",&a[i][j]);
			}
		}
		for(int i=0; i<h; i++){
			for(int j=0; j<w; j++){
				if (a[i][j]==1){
					bfs(i,j);
					c++;
				}
			}
		}
		printf("%d\n",c);
	}
	return 0;
}
