import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int x = 1000 - Integer.parseInt(br.readLine());
        int cnt = 0;
        int m[] = {500, 100, 50, 10, 5, 1};

        for(int i=0; i<m.length; i++){
            cnt+=x/m[i];
            x = x%m[i];
        }
        bw.write(cnt+"");
        bw.flush();
        bw.close();
    }
}
