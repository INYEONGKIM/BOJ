import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String s[]=br.readLine().trim().split(" ");
        int n = Integer.parseInt(s[0]);
        int x = Integer.parseInt(s[1]);
        int cnt = 0;
        int m[] = new int[n];
        for(int i=0; i<n; i++){
            m[i] = Integer.parseInt(br.readLine());
        }
        for(int i=m.length-1; i>=0; i--){
            cnt+=x/m[i];
            x = x%m[i];
        }
        bw.write(cnt+"");
        bw.flush();
        bw.close();
    }
}
