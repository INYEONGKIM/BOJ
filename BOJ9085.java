import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int size=Integer.parseInt(br.readLine());
        int n,sum;
        String s[];
        while(size-->0){
            sum=0;
            n=Integer.parseInt(br.readLine());
            s=br.readLine().split(" ");
            for(int i=0; i<n; i++){
                sum+=Integer.parseInt(s[i]);
            }
            bw.write(sum+"\n");
        }
        bw.flush();
        bw.close();
    }
}
