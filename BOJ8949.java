import java.io.*;
import java.util.LinkedList;
import java.util.Queue;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        Queue<Integer> q = new LinkedList<>();
        String s[]=br.readLine().split(" ");
        int flag=1;
        if(s[0].length()>s[1].length()) flag=0;

        for(int i=0; i<s[flag].length()-s[1-flag].length(); i++){
            q.offer(s[flag].charAt(i)-'0');
        }
        for(int i=s[flag].length()-s[1-flag].length(); i<s[flag].length(); i++){
            q.offer((s[flag].charAt(i)-'0') + (s[1-flag].charAt(i-(s[flag].length()-s[1-flag].length()))-'0'));
        }
        while(!q.isEmpty()){
            bw.write(q.poll()+"");
        }
        bw.flush();
        bw.close();
    }
}
