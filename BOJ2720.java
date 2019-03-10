package test;

import java.io.*;

public class BOJ2720 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int n=Integer.parseInt(br.readLine());
        int change;
        while(n-->0){
            change=Integer.parseInt(br.readLine());
            bw.write(change/25 +" " +(change%25)/10 + " " + ((change%25)%10)/5 +" "+((change%25)%10)%5+"\n");
        }
        bw.flush();
        bw.close();
    }
}