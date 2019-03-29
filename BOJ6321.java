import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        char set[] = {'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A'};
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int len,n = Integer.parseInt(br.readLine());
        String s;
        for(int j=1; j<=n; j++){
            sb.append("String #"+j+"\n");
            s=br.readLine();
            len = s.length();
            for(int i=0; i<len; i++){
                sb.append(set[s.charAt(i)-'A']);
            }
            sb.append("\n\n");
        }
        System.out.println(sb);
    }
}
