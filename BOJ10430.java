import java.io.*;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String s = br.readLine();
        StringTokenizer st = new StringTokenizer(s);
        int a = Integer.parseInt(st.nextToken());
        int b = Integer.parseInt(st.nextToken());
        int c = Integer.parseInt(st.nextToken());

        bw.write((a+b)%c+"\n");
        bw.write(((a%c)+(b%c))%c +"\n");
        bw.write((a*b)%c+"\n");
        bw.write(((a%c)*(b%c))%c +"\n");

        bw.flush();
        bw.close();
    }
}
