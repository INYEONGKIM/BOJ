import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int n = Integer.parseInt(br.readLine());
        String s[];
        while(n-->0){
            s = br.readLine().trim().split(" ");
            for(int i=0; i<s.length; i++){
                bw.write(s[(i+2)%s.length]+" ");
            }
            bw.write("\n");
        }

        bw.flush();
        bw.close();
    }
}
