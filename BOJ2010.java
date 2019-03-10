import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int n=Integer.parseInt(br.readLine());
        int tot=0,m=n;
        while(n-->0){
            tot+=Integer.parseInt(br.readLine());
        }
        bw.write(tot-m+1+"");
        bw.flush();
        bw.close();
    }
}
