import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String s="";
        int sum;
        do{
            s=br.readLine();
            sum=0;
            if(!s.equals("#")){
                for(int i=0; i<s.length(); i++){
                    if(s.charAt(i)!=' ') sum+=((i+1)*(s.charAt(i)-'A'+1));
                }
                bw.write(sum+"\n");
            }
        }while(!s.equals("#"));
        bw.flush();
        bw.close();
    }
}
