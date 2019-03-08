package test;

import java.io.*;

public class BOJ1550 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String s=br.readLine();
        bw.write(Integer.parseInt(s,16)+"");
        bw.flush();
        bw.close();
    }
}