import java.io.*;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int n = Integer.parseInt(br.readLine());
        String s[];
        int a[] = new int[n];
        s = br.readLine().split(" ");
        for(int i=0; i<n; i++){
            a[i]=Integer.parseInt(s[i]);
        }
        Arrays.sort(a);
        bw.write(a[0]+" "+a[a.length-1]);
        bw.flush();
        bw.close();
    }
}
