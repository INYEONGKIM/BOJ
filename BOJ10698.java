import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String s[];
        int n=Integer.parseInt(br.readLine());
        for(int i=1; i<=n; i++){
            s=br.readLine().split(" ");
            if(s[1].equals("+")){
                if(Integer.parseInt(s[0])+Integer.parseInt(s[2]) == Integer.parseInt(s[4]))
                    bw.write("Case "+i+": YES\n");
                else
                    bw.write("Case "+i+": NO\n");
            }else{
                if(Integer.parseInt(s[0])-Integer.parseInt(s[2]) == Integer.parseInt(s[4]))
                    bw.write("Case "+i+": YES\n");
                else
                    bw.write("Case "+i+": NO\n");
            }
        }
        bw.flush();
        bw.close();
    }
}
