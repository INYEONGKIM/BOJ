import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String s=br.readLine();
        String key=br.readLine();
        int gap, keyLen=key.length();
        char temp;
        for(int i=0; i<s.length(); i++){
            temp=s.charAt(i);
            if(temp==' '){
                bw.write(' ');
            }else{
                gap = (key.charAt(i%keyLen)-96);
                if(temp-gap<'a')
                    bw.write(temp-gap+26);
                else
                    bw.write(temp-gap);
            }
        }
        bw.flush();
        bw.close();
    }
}
