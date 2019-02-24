import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int n = Integer.parseInt(br.readLine());
        String s[];
        int a,b;
        for(int i=1; i<=n; i++){
            s=br.readLine().split(" ");
            a = Integer.parseInt(s[0]);
            b = Integer.parseInt(s[1]);
            bw.write("Case #"+i+": "+(a+b)+"\n");
        }
        bw.flush();
        bw.close();
    }
}
