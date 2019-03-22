import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String s;
        String s1[];
        while (true){
            s=br.readLine();
            if(s.equals("0 0")) break;
            s1=s.split(" ");
            bw.write(2*Integer.parseInt(s1[0])-Integer.parseInt(s1[1])+"\n");
        }
        bw.flush();
        bw.close();
    }
}
