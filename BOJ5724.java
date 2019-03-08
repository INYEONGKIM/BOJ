package test;

import java.io.*;

public class BOJ5724 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int n;
        while(true){
            n=Integer.parseInt(br.readLine());
            if(n==0) break;
            bw.write((n*(n+1)*(2*n+1))/6+"\n");
        }
        bw.flush();
        bw.close();
    }
}
