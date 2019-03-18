import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String s=br.readLine();
        boolean flag=true;
        int l=0, r=s.length()-1;
        while(l<=r){
            if(s.charAt(l)!=s.charAt(r)){
                flag=false;
                break;
            }else{
                l++;
                r--;
            }
        }
        bw.write(flag+"");
        bw.flush();
        bw.close();
    }
}
