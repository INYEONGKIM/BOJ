import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String s=br.readLine();
        long a,b;
        boolean flag=false;
        for(int i=1; i<s.length(); i++){
            a=1; b=1;
            for(int j=0; j<i; j++){
                a*=(s.charAt(j)-'0');
            }
            for(int j=i; j<s.length(); j++){
                b*=(s.charAt(j)-'0');
            }
            if(a==b){
                flag=true;
                break;
            }
        }
        System.out.printf("%s", flag?"YES":"NO");
    }
}
