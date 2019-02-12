import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String s;
        int cnt=0;
        for(int i=0; i<8; i++){
            s=br.readLine();
            if(i%2==0){
                for(int j=0; j<8; j+=2){
                    if(s.charAt(j)=='F') cnt++;
                }
            }else{
                for(int j=1; j<8; j+=2){
                    if(s.charAt(j)=='F') cnt++;
                }
            }
        }
        System.out.println(cnt);
    }
}
