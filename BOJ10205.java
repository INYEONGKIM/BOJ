import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String s;
        int head,len,n=Integer.parseInt(br.readLine());
        for(int i=1; i<=n; i++){
            head=Integer.parseInt(br.readLine());
            s=br.readLine();
            len=s.length();
            for(int j=0; j<len; j++){
                if(s.charAt(j)=='c') head++;
                else if(s.charAt(j)=='b') head--;
            }
            bw.write("Data Set "+i+":\n"+head+"\n\n");
        }
        bw.flush();
        bw.close();
    }
}
