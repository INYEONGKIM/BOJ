import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int len,n=Integer.parseInt(br.readLine());
        String s[];
        while(n-->0){
            s=br.readLine().split(" ");
            len=Integer.parseInt(s[0]);
            if (s[1].equals("C")){
                s=br.readLine().split(" ");
                for(int i=0; i<len; i++){
                    bw.write((s[i].charAt(0)-'A'+1)+" ");
                }
            }else{
                s=br.readLine().split(" ");
                for(int i=0; i<len; i++){
                    bw.write((char) ('A'+Integer.parseInt(s[i])-1)+" ");
                }
            }
            bw.write("\n");
        }
        bw.flush();
        bw.close();
    }
}
