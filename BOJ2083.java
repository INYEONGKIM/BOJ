package test;

import java.io.*;

public class BOJ2083 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String s=br.readLine().trim();
        String s1[];
        while(true){
            if(s.equals("# 0 0")) break;
            s1=s.split(" ");
            bw.write(s1[0]+String.format(" %s\n", (Integer.parseInt(s1[1])>17 || Integer.parseInt(s1[2])>=80)?"Senior":"Junior"));
            s=br.readLine().trim();
        }
        bw.flush();
        bw.close();
    }
}
