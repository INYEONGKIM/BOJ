import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        long n = Long.parseLong(br.readLine());
        int f0=0, f1=1, f2=1, repeat=0;
        for(int i=2; i<=n; i++){
            f2 = (f1+f0)%1000000;
            if(f2%1000000==1 && f1%1000000==0){
                repeat = i-1;
                break;
            }
            f0 = f1;
            f1 = f2;
        }
        if(repeat>0){
            int newN = (int)(n%repeat);
            f0=0;
            f1=1;
            f2=1;
            for(int i=2; i<=newN; i++){
                f2 = (f1+f0)%1000000;
                f0 = f1;
                f1 = f2;
            }
        }
        bw.write(f2+"");
        bw.flush();
        bw.close();
    }
}
