import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        char c[][] = new char[5][15];
        String s;

        for(int i=0; i<5; i++){
            s = br.readLine();
            for(int j=0; j<s.length(); j++){
                c[i][j] = s.charAt(j);
            }
        }

        for(int i=0; i<15; i++){
            for(int j=0; j<5; j++){
                if(c[j][i]!='\u0000') bw.write(c[j][i]+"");
            }
        }

        bw.flush();
        bw.close();
    }
}
