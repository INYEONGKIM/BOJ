import java.io.*;

public class Main {
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		String[] s = br.readLine().split(" ");
		int[] a = new int[n];
		for(int i=0; i<n; i++) {
			a[i]=Integer.parseInt(s[i]);
		}
		
		int[] d = new int[n];
		d[0]=1;
		for(int i=1; i<n; i++) {
			d[i]=1;
			for(int j=0; j<i; j++) {
				if(d[i]<=d[j] && a[i]<a[j]) {
					d[i]=d[j]+1;
				}else if(a[i]==a[j]) {
					d[i]=d[j];
				}
			}
		}
		int m = d[0];
		for(int i=1; i<n; i++) {
			m=Math.max(m, d[i]);
		}
		System.out.println(m);
	}
}
