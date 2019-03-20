import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String s[]=br.readLine().split(" ");
        int a=Integer.parseInt(s[0]);
        int b=Integer.parseInt(s[1]);
        int c[]=new int[b];
        int cnt=1,n=1, res=0;
        for(int i=0; i<b; i++){
            c[i]=n;
            if(cnt==n){
                n++;
                cnt=1;
            }else{
                cnt++;
            }
        }
        for(int i=a-1; i<=b-1; i++){
            res+=c[i];
        }
        bw.write(res+"");
        bw.flush();
        bw.close();
    }
}
