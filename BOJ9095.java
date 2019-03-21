import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int a[]=new int[11];
        a[0]=0;
        a[1]=1;
        a[2]=2;
        a[3]=4;
        for(int i=4; i<11; i++){
            a[i]=a[i-1]+a[i-2]+a[i-3];
        }
        int n=Integer.parseInt(br.readLine());
        while(n-->0){
            bw.write(a[Integer.parseInt(br.readLine())]+"\n");
        }
        bw.flush();
        bw.close();
    }
}
