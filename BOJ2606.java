import java.io.*;
import java.util.LinkedList;
import java.util.Queue;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int a,b,m=Integer.parseInt(br.readLine());
        int com[][]=new int[n][n];

        String s[];
        while(m-->0){
            s=br.readLine().split(" ");
            a=Integer.parseInt(s[0])-1;
            b=Integer.parseInt(s[1])-1;
            com[a][b]=com[b][a]=1;
        }
        System.out.println(bfs(com, n));
    }

    public static int bfs(int com[][], int size){
        boolean visit[] = new boolean[size];
        int cnt=0;
        Queue<Integer> q = new LinkedList<>();
        q.offer(0);
        while(!q.isEmpty()){
            int x=q.poll();
            visit[x]=true;
            for(int i=0; i<size; i++){
                if(com[x][i]==1 && !visit[i]){
                    q.offer(i);
                    visit[i]=true;
                    cnt++;
                }
            }
        }
        return cnt;
    }
}
