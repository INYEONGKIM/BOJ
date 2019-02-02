import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int n = Integer.parseInt(br.readLine());
        char c[];
        int num;
        while(n-->0){
            int res=0;
            c = br.readLine().toCharArray();
            for(int i=0; i<c.length; i++){
                if(i%2==0){
                    num = 2*(c[i]-'0');
                    if(num>=10){
                        res+=(num/10 + num%10);
                    }else{
                        res+=num;
                    }
                }else{
                    res+=(c[i]-'0');
                }
            }
            if(res%10==0)
                bw.write("T\n");
            else
                bw.write("F\n");
        }
        bw.flush();
        bw.close();
    }
}
