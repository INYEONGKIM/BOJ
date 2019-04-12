import java.io.*;
import java.math.BigInteger;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        for (int i = 0; i < 3; i++) {
            int n = Integer.parseInt(br.readLine());
            BigInteger sum = new BigInteger("0");
            for (int j = 0; j < n; j++) sum = sum.add(new BigInteger(br.readLine()));
            if (sum.signum() < 0) bw.write("-\n");
            else if (sum.signum() == 0) bw.write("0\n");
            else bw.write("+\n");
        }
        bw.flush();
        bw.close();
    }
}
