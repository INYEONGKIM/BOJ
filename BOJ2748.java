import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int n=Integer.parseInt(br.readLine());
        long a[]=new long[n+1];
        a[0]=0;
        a[1]=1;
        for(int i=2; i<=n; i++){
            a[i]=a[i-1]+a[i-2];
        }
        bw.write(a[n]+"");
        bw.flush();
        bw.close();
    }
}
