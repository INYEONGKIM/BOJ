import java.io.*;
import java.util.HashSet;
import java.util.Set;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        char s[];
        int res = 0;
        while(n-->0){
            int cnt=1;
            s=br.readLine().toCharArray();
            Set<Character> set = new HashSet<>();
            char c = s[0];
            set.add(s[0]);

            for(int i=1; i<s.length; i++){
                set.add(s[i]);
                if(c!=s[i]){
                    cnt++;
                    c=s[i];
                }
            }
            if(set.size()==cnt) res++;
        }
        System.out.print(res);
    }
}
