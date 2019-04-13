import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String s[] = br.readLine().split(" ");
        int n = Integer.parseInt(s[0]);
        int cnt = Integer.parseInt(s[1]);
        int a[]=new int[n];
        s=br.readLine().split(" ");
        a[0]=Integer.parseInt(s[0]);
        for(int i=1; i<n; i++){
            a[i]=a[i-1]+Integer.parseInt(s[i]);
        }

        while(cnt-->0){
            s=br.readLine().split(" ");
            int end = Integer.parseInt(s[1])-1;
            int start = Integer.parseInt(s[0])-1;
            if(start==0)
                bw.write(a[end]+"\n");
            else
                bw.write((a[end]-a[start-1])+"\n");
        }
        bw.flush();
        bw.close();
    }
}
