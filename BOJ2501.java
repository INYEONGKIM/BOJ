import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String s[]=br.readLine().split(" ");
        int cnt=0,p=Integer.parseInt(s[0]), q=Integer.parseInt(s[1]);
        int a[]=new int[p];
        for(int i=1; i<=p; i++){
            if(p%i==0){
                a[cnt++]=i;
            }
        }
        bw.write(a[q-1]+"");
        bw.flush();
        bw.close();
    }
}
