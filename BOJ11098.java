import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int n,m=Integer.parseInt(br.readLine());
        String s[];
        String top;
        int topM;
        while(m-->0){
            n=Integer.parseInt(br.readLine());
            s=br.readLine().split(" ");
            topM=Integer.parseInt(s[0]);
            top=s[1];
            n--;
            while(n-->0){
                s=br.readLine().split(" ");
                if(topM<Integer.parseInt(s[0])){
                    topM=Integer.parseInt(s[0]);
                    top=s[1];
                }
            }
            bw.write(top+"\n");
        }
        bw.flush();
        bw.close();
    }
}
