import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String s[];
        int n=Integer.parseInt(br.readLine());
        while(n-->0){
            s=br.readLine().split(" ");
            bw.write(2+Integer.parseInt(s[1])-Integer.parseInt(s[0])+"\n");
        }
        bw.flush();
        bw.close();
    }
}
