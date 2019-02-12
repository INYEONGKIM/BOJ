import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int temp,cnt=0;
        String s = br.readLine();
        while(s.length()>1){
            temp=0;
            cnt++;
            for(int i=0; i<s.length(); i++){
                temp+=(s.charAt(i)-'0');
            }
            s=String.valueOf(temp);
        }
        System.out.println(cnt);
        System.out.printf("%s",(s.equals("3")||s.equals("6")||s.equals("9")?"YES":"NO"));
    }
}
