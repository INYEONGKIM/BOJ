import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br =  new BufferedReader(new InputStreamReader(System.in));
        String s = br.readLine().trim();
        char c[] = s.toCharArray();
        for(int i=0; i<c.length; i++){

            if(c[i]<='C'){
                System.out.printf("%c", c[i]+23);
            }else{
                System.out.printf("%c", c[i]-3);
            }
        }
    }
}
