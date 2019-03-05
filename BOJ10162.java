import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int n=Integer.parseInt(br.readLine());
        if(n%10!=0){
            bw.write("-1");
        }else{
            bw.write(n/300+" ");
            n%=300;
            bw.write(n/60+" ");
            n%=60;
            bw.write(n/10+"");
        }
        bw.flush();
        bw.close();
    }
}
