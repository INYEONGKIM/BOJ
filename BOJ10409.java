import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String s[];
        s=br.readLine().split(" ");
        int len=Integer.parseInt(s[0]);
        int cnt=0,sum=0,max=Integer.parseInt(s[1]);
        s=br.readLine().split(" ");
        for(int i=0; i<len; i++){
            sum+=Integer.parseInt(s[i]);
            if(sum<=max){
                cnt++;
            }else{
                break;
            }
        }
        bw.write(cnt+"");
        bw.flush();
        bw.close();
    }
}
