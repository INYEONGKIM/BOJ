import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int n=Integer.parseInt(br.readLine());
        String s[];
        while(n-->0){
            s=br.readLine().split("\\+");
            if(s[0].equals("P=NP")){
                bw.write("skipped\n");
            }else{
                bw.write(Integer.parseInt(s[0])+Integer.parseInt(s[1])+"\n");
            }
        }
        bw.flush();
        bw.close();
    }
}
