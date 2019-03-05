import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String s[]=br.readLine().split(" ");
        bw.write(Double.parseDouble(s[0])/Double.parseDouble(s[1])+"");
        bw.flush();
        bw.close();
    }
}
