import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String s;
        while(!((s=br.readLine()).equals("***"))){
            for(int i=s.length()-1; i>=0; i--){
                bw.write(s.charAt(i));
            }
            bw.write("\n");
        }

        bw.flush();
        bw.close();
    }
}
