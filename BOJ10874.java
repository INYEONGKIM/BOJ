package test;

import java.io.*;

public class BOJ10874 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String s,ans="1 2 3 4 5 1 2 3 4 5";
        int n=Integer.parseInt(br.readLine());
        for(int i=1; i<=n; i++){
            s=br.readLine();
            if(s.equals(ans)) bw.write(i+"\n");
        }
        bw.flush();
        bw.close();
    }
}