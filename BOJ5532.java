import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int L = Integer.parseInt(br.readLine());
        int A = Integer.parseInt(br.readLine());
        int B = Integer.parseInt(br.readLine());
        int C = Integer.parseInt(br.readLine());
        int D = Integer.parseInt(br.readLine());

        int M,E;
        if(A%C == 0) M=A/C;
        else M=(A/C)+1;
        if(B%D == 0) E=B/D;
        else E=(B/D)+1;
        int res = Math.max(M,E);
        System.out.printf("%d", (res>L ? 0 : L-res));
    }
}
