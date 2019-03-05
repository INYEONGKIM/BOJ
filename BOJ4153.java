import java.io.*;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String s[];
        int sum;
        int a[]=new int[3];
        do{
            sum=0;
            s=br.readLine().split(" ");
            for(int i=0; i<3; i++){
                a[i]=Integer.parseInt(s[i]);
                sum+=a[i];
            }
            if(sum==0){
                break;
            }else{
                Arrays.sort(a);
                if(a[2]*a[2]==(a[1]*a[1] + a[0]*a[0]))
                    bw.write("right\n");
                else
                    bw.write("wrong\n");
            }
        }while(sum!=0);
        bw.flush();
        bw.close();
    }
}
