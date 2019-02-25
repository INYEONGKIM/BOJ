import java.io.*;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int a[] = new int[5];
        int sum=0;
        for(int i=0; i<5; i++){
            a[i]=Integer.parseInt(br.readLine());
            sum+=a[i];
        }
        Arrays.sort(a);
        bw.write(sum/5+"\n"+a[2]);

        bw.flush();
        bw.close();
    }
}
