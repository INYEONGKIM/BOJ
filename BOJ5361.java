import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        String s[];
        double sum;
        int n = Integer.parseInt(br.readLine());
        while(n-->0){
            sum=0;
            s=br.readLine().split(" ");
            sum += (350.34*Integer.parseInt(s[0]) + 230.90*Integer.parseInt(s[1]) + 190.55*Integer.parseInt(s[2]) + 125.30*Integer.parseInt(s[3]) + 180.90*Integer.parseInt(s[4]));
            sb.append("$"+String.format("%.2f",sum)+"\n");
        }
        System.out.println(sb);
    }
}
