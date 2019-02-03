import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int a[] = new int[26];
        for(int i=0; i<a.length; i++){
            a[i]=-1;
        }
        char c[] = br.readLine().toCharArray();
        for(int i=0; i<c.length; i++){
            if(a[c[i]-'a']==-1) a[c[i]-'a']=i;
        }
        for(int i=0; i<a.length; i++){
            bw.write(a[i]+" ");
        }
        bw.flush();
        bw.close();
    }
}
