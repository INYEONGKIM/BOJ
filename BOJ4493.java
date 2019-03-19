package test;

import java.io.*;

public class BOJ4493 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int n,cnt,m=Integer.parseInt(br.readLine());
        String s;
        int p1;
        while(m-->0){
            p1=0;
            n=Integer.parseInt(br.readLine());
            cnt=n;
            while(n-->0){
                s=br.readLine().trim();
                if(s.equals("R R") || s.equals("S S") || s.equals("P P")) cnt--;
                if(s.equals("R S") || s.equals("S P") || s.equals("P R")) p1++;
            }
            if(cnt%2==0){
                if(cnt/2==p1){
                    bw.write("TIE\n");
                }else if(cnt/2<p1){
                    bw.write("Player 1\n");
                }else{
                    bw.write("Player 2\n");
                }
            }else{
                if(cnt/2<p1){
                    bw.write("Player 1\n");
                }else{
                    bw.write("Player 2\n");
                }
            }
        }
        bw.flush();
        bw.close();
    }
}