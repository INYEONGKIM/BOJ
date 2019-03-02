import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String raw = br.readLine();
        String s[] = raw.split("\\.");
        String res = "";
        for(int i=0; i<s.length; i++){
            if(s[i].length()%2 == 1){
                res="-1";
                break;
            }else{
                for(int j=0; j<(s[i].length()/4); j++){
                    res+="AAAA";
                }
                for(int j=0; j<(s[i].length()%4-1); j++){
                    res+="BB";
                }
                if(i!=s.length-1) res+=".";
            }
        }
        int temp=res.length();
        if(!res.equals("-1") && raw.length()!=temp){
            for(int i=0; i<raw.length()-temp; i++){
                res+=".";
            }
        }
        bw.write(res);
        bw.flush();
        bw.close();
    }
}
