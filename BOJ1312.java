import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String s[]=br.readLine().split(" ");
        int A = Integer.parseInt(s[0]);
        int B = Integer.parseInt(s[1]);
        int N = Integer.parseInt(s[2]);
        A%=B;
        for(int i=0; i<N-1; i++){
            A*=10;
            A%=B;
        }
        A*=10;
        bw.write(A/B+"");
        bw.flush();
        bw.close();
    }
}
