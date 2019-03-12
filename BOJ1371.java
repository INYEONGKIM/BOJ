import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int a[] = new int[26];
        String s;
        while ((s = br.readLine()) != null) {
            for (int i = 0; i < s.length(); i++) {
                if (s.charAt(i)>='a' && s.charAt(i)<='z') {
                    a[s.charAt(i)-'a']++;
                }
            }
        }
        int max = 0;
        for (int i = 0; i < 26; i++) {
            max = Math.max(max, a[i]);
        }
        for (int i = 0; i < 26; i++) {
            if (a[i] == max) {
                bw.write('a' + i);
            }
        }
        bw.flush();
        bw.close();
    }
}
