import java.io.*;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String s[]=br.readLine().split(" ");
        int a[]=new int[4];
        for(int i=0; i<4; i++){
            a[i]=Integer.parseInt(s[i]);
        }
        Arrays.sort(a);
        System.out.println(a[0]*a[2]);
    }
}
