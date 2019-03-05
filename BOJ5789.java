import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int n=Integer.parseInt(br.readLine());
        String s;
        while(n-->0){
            s=br.readLine();
            bw.write(String.format("%s", (s.charAt(s.length()/2)==s.charAt(s.length()/2-1))?"Do-it\n":"Do-it-Not\n"));
        }
        bw.flush();
        bw.close();
    }
}
