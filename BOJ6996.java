import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int len,n=Integer.parseInt(br.readLine());
        String s[];
        while(n-->0){
            int a[] = new int[26];
            s=br.readLine().trim().split(" ");
            if(s[0].length()!=s[1].length()){
                bw.write(s[0]+" & "+s[1]+" are NOT anagrams.\n");
            }else{
                len=s[0].length();
                for(int i=0; i<len; i++){
                    a[s[0].charAt(i)-'a']++;
                    a[s[1].charAt(i)-'a']--;
                }
                int i;
                for(i=0; i<26; i++){
                    if(a[i]!=0) break;
                }
                if(i==26)
                    bw.write(s[0]+" & "+s[1]+" are anagrams.\n");
                else
                    bw.write(s[0]+" & "+s[1]+" are NOT anagrams.\n");
            }
        }
        bw.flush();
        bw.close();
    }
}
