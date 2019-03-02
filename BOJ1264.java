import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String s="";
        int cnt;
        char tmp;
        do{
            cnt=0;
            s=br.readLine();
            for(int i=0; i<s.length(); i++){
                tmp=s.charAt(i);
                if(tmp=='a'||tmp=='e'||tmp=='i'||tmp=='o'||tmp=='u'|| tmp=='A'||tmp=='E'||tmp=='I'||tmp=='O'||tmp=='U') cnt++;
            }
            if(!s.equals("#")) bw.write(cnt+"\n");
        }while(!s.equals("#"));
        bw.flush();
        bw.close();
    }
}
