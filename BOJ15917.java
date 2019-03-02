import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int n=Integer.parseInt(br.readLine());
        int a;
        while(n-->0){
            a=Integer.parseInt(br.readLine());
            if((a&(--a))==0)
                bw.write(1+"\n");
            else
                bw.write(0+"\n");
        }
        bw.flush();
        bw.close();
    }
}
