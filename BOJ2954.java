import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String s=br.readLine();
        char c;
        for(int i=0; i<s.length(); i++){
            c=s.charAt(i);
            bw.write(c);
            if(c=='a'||c=='e'||c=='i'||c=='o'||c=='u') i+=2;
        }
        bw.flush();
        bw.close();
    }
}
