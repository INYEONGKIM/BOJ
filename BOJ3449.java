package test;

import java.io.*;

public class BOJ3449 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int cnt,len,n=Integer.parseInt(br.readLine());
        String s1,s2;
        for(int i=1; i<=n; i++){
            cnt=0;
            s1=br.readLine();
            s2=br.readLine();
            len=s1.length();
            for(int j=0; j<len; j++){
                if(s1.charAt(j)!=s2.charAt(j)) cnt++;
            }
            bw.write("Hamming distance is "+cnt+".\n");
        }
        bw.flush();
        bw.close();
    }
}