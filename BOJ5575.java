import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        String s[];
        int t;
        for(int i=0; i<3; i++){
            s=br.readLine().split(" ");
            t = Integer.parseInt(s[3])*3600 + Integer.parseInt(s[4])*60 + Integer.parseInt(s[5])
                    - Integer.parseInt(s[0])*3600 - Integer.parseInt(s[1])*60 - Integer.parseInt(s[2]);
            sb.append(t/3600+" "+(t%3600)/60 + " "+(t%3600)%60+"\n");
        }
        System.out.println(sb);
    }
}
