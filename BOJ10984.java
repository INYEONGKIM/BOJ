package test;

import java.io.*;

public class BOJ10984 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int n,m=Integer.parseInt(br.readLine());
        int cnt=0;
        double gpa=0;
        String s[];
        while(m-->0){
            cnt=0;
            gpa=0;
            n=Integer.parseInt(br.readLine());
            while(n-->0){
                s=br.readLine().split(" ");
                cnt+=Integer.parseInt(s[0]);
                gpa+=Integer.parseInt(s[0])*Double.parseDouble(s[1]);
            }
            bw.write(cnt+" "+String.format("%.1f",gpa/cnt)+"\n");
        }
        bw.flush();
        bw.close();
    }
}