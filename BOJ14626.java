import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        char c[] = br.readLine().toCharArray();
        int idx=-1,sum=0;
        for(int i=0; i<c.length; i++){
            if(c[i]!='*'){
                if(i%2==0)
                    sum+=(c[i]-'0');
                else if(i%2==1)
                    sum+=(3*(c[i]-'0'));
            }else{
                idx = i%2;
            }
        }
        for(int i=0; i<10; i++){
            if((sum + i*(idx==0?1:3))%10 == 0){
                System.out.println(i);
                break;
            }
        }
    }
}
