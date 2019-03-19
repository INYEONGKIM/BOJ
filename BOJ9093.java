import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int size,n=Integer.parseInt(br.readLine());
        String s[];
        while(n-->0){
            s=br.readLine().trim().split(" ");
            size=s.length;
            for(int i=0; i<size; i++){
                StringBuffer sb = new StringBuffer(s[i]);
                bw.write(sb.reverse()+" ");
            }
            bw.write("\n");
        }
        bw.flush();
        bw.close();
    }
}
