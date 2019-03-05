import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int n=Integer.parseInt(br.readLine());
        String s1,s2;
        int len,cnt;
        for(int i=1; i<=n; i++){
            cnt=0;
            len=Integer.parseInt(br.readLine());
            s1=br.readLine();
            s2=br.readLine();
            for(int j=0; j<len; j++){
                if(s1.charAt(j)!=s2.charAt(j)) cnt++;
            }
            bw.write("Case "+i+": "+cnt+"\n");
        }
        bw.flush();
        bw.close();
    }
}
