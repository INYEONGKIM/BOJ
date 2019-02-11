import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String s = br.readLine().trim();
        while(s.length()!=1 || s.charAt(0)!='#'){
            int res=0;
            for(int i=0; i<s.length(); i++){
                switch (s.charAt(i)){
                    case '-':
                        res+=0;
                        break;
                    case '\\':
                        res+=(Math.pow(8,s.length()-i-1));
                        break;
                    case '(':
                        res+=(2*Math.pow(8,s.length()-i-1));
                        break;
                    case '@':
                        res+=(3*Math.pow(8,s.length()-i-1));
                        break;
                    case '?':
                        res+=(4*Math.pow(8,s.length()-i-1));
                        break;
                    case '>':
                        res+=(5*Math.pow(8,s.length()-i-1));
                        break;
                    case '&':
                        res+=(6*Math.pow(8,s.length()-i-1));
                        break;
                    case '%':
                        res+=(7*Math.pow(8,s.length()-i-1));
                        break;
                    case '/':
                        res+=(-1*Math.pow(8,s.length()-i-1));
                        break;
                }
            }
            System.out.println(res);
            s = br.readLine().trim();
        }
    }
}
