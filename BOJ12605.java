import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String s[];
        int size,n=Integer.parseInt(br.readLine());
        for(int i=1; i<=n; i++){
            s=br.readLine().trim().split(" ");
            size=s.length;
            bw.write("Case #"+i+": ");
            for(int j=size-1; j>0; j--){
                bw.write(s[j]+" ");
            }
            bw.write(s[0]+"\n");
        }
        bw.flush();
        bw.close();
    }
}
