import java.io.*;

public class Main {
	static int[] a;
	static int[] v;
	static String go(int p) {
		if (p == -1) {
			return "";
		}
		return go(v[p]) + " " + a[p];
	}

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		String[] s = br.readLine().split(" ");
		a = new int[n];
		int[] d = new int[n];
		v = new int[n];
		for (int i = 0; i < n; i++) {
			a[i] = Integer.parseInt(s[i]);
			v[i] = -1;
		}
		int max = 1;
		int idx = 0;
		for (int i = 0; i < n; i++) {
			d[i] = 1;
			for (int j = 0; j < i; j++) {
				if (a[j] < a[i] && d[j] >= d[i]) {
					d[i] = d[j] + 1;
					v[i] = j;
					if (d[i] > max) {
						max = d[i];
						idx = i;
					}
				}
			}
		}
		System.out.println(max);
		System.out.println(go(idx).trim());
	}
}
