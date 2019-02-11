import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        char c[] = new char[26];
        String s,a;
        int n =Integer.parseInt(br.readLine());
        while(n-->0){
            s = br.readLine();
            a = br.readLine().trim();
            for(int i=0; i<26; i++){
                c[i]=a.charAt(i);
            }
            for(int i=0; i<s.length(); i++){
                if(s.charAt(i)==' ')
                    bw.write(" ");
                else
                    bw.write(c[s.charAt(i)-'A']+"");
            }
            bw.write("\n");
            bw.flush();
        }
        bw.close();
    }
}
