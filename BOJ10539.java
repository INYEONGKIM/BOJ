import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int n=Integer.parseInt(br.readLine());
        int a[]=new int[n];
        int sum=0;
        String s[]=br.readLine().split(" ");
        for(int i=0; i<n; i++){
            a[i]=Integer.parseInt(s[i]);
            bw.write((i+1)*a[i]-sum +" ");
            sum+=((i+1)*a[i]-sum);
        }
        bw.flush();
        bw.close();
    }
}
