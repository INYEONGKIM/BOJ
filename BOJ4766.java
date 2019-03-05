import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        double a,b = Double.parseDouble(br.readLine());
        while(b!=999){
            a=Double.parseDouble(br.readLine());
            if(a!=999) bw.write(String.format("%.2f",a-b)+"\n");
            b=a;
        }
        bw.flush();
        bw.close();
    }
}
