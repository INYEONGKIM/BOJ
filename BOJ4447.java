import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int n = Integer.parseInt(br.readLine());
        String s;
        while(n-->0){
            s = br.readLine();
            int g=0,b=0;
            for(int i=0; i<s.length(); i++){
                if(s.charAt(i)=='g' || s.charAt(i)=='G') g++;
                if(s.charAt(i)=='b' || s.charAt(i)=='B') b++;
            }
            bw.write(s+" is ");
            if(g==b)
                bw.write("NEUTRAL\n");
            else if(g>b)
                bw.write("GOOD\n");
            else
                bw.write("A BADDY\n");

        }
        bw.flush();
        bw.close();
    }
}
