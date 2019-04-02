import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String s[];
        int x,y,n=Integer.parseInt(br.readLine());
        while(n-->0){
            s=br.readLine().split(" ");
            x=Integer.parseInt(s[0]);
            y=Integer.parseInt(s[1]);
            bw.write("You get "+(x/y)+" piece(s) and your dad gets "+x%y+" piece(s).\n");
        }
        bw.flush();
        bw.close();
    }
}
