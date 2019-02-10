import java.io.*;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int n=Integer.parseInt(br.readLine());
        String s[] = br.readLine().trim().split(" ");
        int a[] = new int[n];
        for(int i=0; i<s.length; i++){
            a[i]=Integer.parseInt(s[i]);
        }
        Arrays.sort(a);
        int res=0;
        for(int i=0; i<a.length; i++){
            res+=(a[i]*(n--));
        }
        bw.write(res+"");
        bw.flush();
        bw.close();
    }
}
