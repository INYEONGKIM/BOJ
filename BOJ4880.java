import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String raw,s[];
        int a,b,d;

        while(true){
            raw = br.readLine();
            if(raw.equals("0 0 0")) break;
            s=raw.split(" ");
            a = Integer.parseInt(s[0]);
            b = Integer.parseInt(s[1]);
            d = b-a;
            if(b+d != Integer.parseInt(s[2])){
                bw.write("GP "+ b*(b/a)*(b/a)+"\n");
            }else{
                bw.write("AP "+(a+3*d)+"\n");
            }
        }
        bw.flush();
        bw.close();
    }
}
