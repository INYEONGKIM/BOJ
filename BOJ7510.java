import java.io.*;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int n = Integer.parseInt(br.readLine());
        int a[] = new int[3];
        String s[];
        for(int i=1; i<=n; i++){
            s = br.readLine().split(" ");
            a[0] = Integer.parseInt(s[0]);
            a[1] = Integer.parseInt(s[1]);
            a[2] = Integer.parseInt(s[2]);
            Arrays.sort(a);
            bw.write("Scenario #"+i+":\n");
            if(a[2]*a[2] == (a[0]*a[0] + a[1]*a[1]))
                bw.write("yes\n\n");
            else
                bw.write("no\n\n");
        }

        bw.flush();
        bw.close();
    }
}
