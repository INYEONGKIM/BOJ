import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String s[] = br.readLine().split(" ");
        bw.write(Math.abs((Long.parseLong(s[0])-Long.parseLong(s[1])))+"");
        bw.flush();
        bw.close();
    }
}
