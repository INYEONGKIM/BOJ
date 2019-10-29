import java.io.*;

public class Main {
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		int res=1;
		String[] s = br.readLine().split(" ");
		int[][] d = new int[n][3];
		for(int i=0; i<n; i++) {
			int x = Integer.parseInt(s[i]);
			d[i][0]=x;
			d[i][1]=1;
			d[i][2]=1;
			
			for(int j=0; j<i; j++) {
				if(d[j][0]<x) {
					d[i][1]=Math.max(d[i][1], d[j][1]+1);
				}
				if(d[j][0]>x) {
					d[i][2]=Math.max(d[i][2], d[j][2]+1);
					d[i][2]=Math.max(d[i][2], d[j][1]+1);
				}
			}
			res=Math.max(res, Math.max(d[i][1], d[i][2]));
		}
		System.out.println(res);
	}
}
