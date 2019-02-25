import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int n = Integer.parseInt(br.readLine());
        String s;
        while(n-->0){
            s=br.readLine();
            if(s.charAt(0)>='a' && s.charAt(0)<='z') bw.write((s.charAt(0)-' '));
            else bw.write(s.charAt(0));
            for(int i=1; i<s.length(); i++){
                bw.write(s.charAt(i));
            }
            bw.write("\n");
        }
        bw.flush();
        bw.close();
    }
}
