import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String s,s1,rev,res;
        int n=Integer.parseInt(br.readLine());
        while(n-->0){
            s=br.readLine();
            s1=reverse(s);
            res = String.valueOf(Integer.parseInt(s)+Integer.parseInt(s1));
            rev = reverse(res);
            if(res.equals(rev))
                bw.write("YES\n");
            else
                bw.write("NO\n");
        }
        bw.flush();
        bw.close();
    }
    public static String reverse(String s){
        return (new StringBuilder(s)).reverse().toString();
    }
}
