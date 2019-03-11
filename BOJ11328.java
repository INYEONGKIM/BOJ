import java.io.*;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String s[];
        char c1[], c2[];
        int len,n=Integer.parseInt(br.readLine());
        while(n-->0){
            s=br.readLine().split(" ");
            if(s[0].length()!=s[1].length()){
                bw.write("Impossible\n");
            }else{
                c1=s[0].toCharArray();
                c2=s[1].toCharArray();
                Arrays.sort(c1);
                Arrays.sort(c2);
                len=c1.length;
                for(int i=0; i<len; i++){
                    if(c1[i]!=c2[i]){
                        bw.write("Impossible\n");
                        break;
                    }
                    if(i==len-1) bw.write("Possible\n");
                }
            }
        }
        bw.flush();
        bw.close();
    }
}
