import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String input="";
        String s[];
        while((input=br.readLine())!=null){
            s=input.split(" ");
            bw.write(Integer.parseInt(s[0])+Integer.parseInt(s[1])+"\n");
        }
        bw.flush();
        bw.close();
    }
}
