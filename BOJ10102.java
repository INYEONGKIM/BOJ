import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n=Integer.parseInt(br.readLine());
        String s=br.readLine();
        int cnt=0;
        for(int i=0; i<n; i++){
            if(s.charAt(i)=='A') cnt++;
        }
        if(n%2==0 && n/2==cnt) System.out.println("Tie");
        else System.out.printf("%c", (cnt>n/2) ? 'A':'B');
    }
}
