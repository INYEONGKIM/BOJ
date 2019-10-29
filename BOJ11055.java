import java.io.*;

public class Main {
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		String[] s = br.readLine().split(" ");
		int[] a = new int[n];
		int[] d = new int[n];
		int res=1;
		for(int i=0; i<n; i++) {
			a[i]=Integer.parseInt(s[i]);
			d[i]=a[i];
			for(int j=0; j<i; j++) {
				if(a[j]<a[i] && d[i]<=d[j]+a[i]) {
					d[i]=d[j]+a[i];
				}
			}
			res=Math.max(res, d[i]);
		}
		System.out.println(res);
	}
}
