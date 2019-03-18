import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int a[] = new int[1000];
        int cnt=0, num=1, res=0;
        for(int i=0; i<1000; i++){
            cnt++;
            a[i] = num;
            if(cnt==num) {
                num++;
                cnt = 0;
            }
        }
        String s[]=br.readLine().split(" ");
        int start = Integer.parseInt(s[0])-1;
        int end = Integer.parseInt(s[1])-1;
        for(int i=start; i<=end; i++){
            res+=a[i];
        }
        bw.write(res+"");
        bw.flush();
        bw.close();
    }
}
