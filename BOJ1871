import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int n = Integer.parseInt(br.readLine());
        String s[];
        while(n-->0){
            int a=0;
            s=br.readLine().split("-");
            for(int i=2; i>=0; i--){
                a+=(Math.pow(26,i)*(s[0].charAt(2-i)-'A'));
            }
            if(Math.abs(a-Integer.parseInt(s[1]))<=100)
                bw.write("nice\n");
            else
                bw.write("not nice\n");
        }
        bw.flush();
        bw.close();
    }
}
