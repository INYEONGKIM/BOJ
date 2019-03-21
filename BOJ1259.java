import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String s;
        boolean flag;
        int l,r;
        while (true){
            s=br.readLine();
            if(s.equals("0")) break;
            flag=true;
            l=0; r=s.length()-1;
            while(l<r){
                if(s.charAt(l)!=s.charAt(r)){
                    flag=false;
                    break;
                }
                l++;
                r--;
            }
            bw.write(String.format("%s\n", flag?"yes":"no"));
        }
        bw.flush();
        bw.close();
    }
}
