package test;

import java.io.*;

public class BOJ4597 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String s=br.readLine();
        int cnt,len;
        while(true){
            if(s.equals("#")) break;
            len=s.length()-1;
            cnt=0;
            for(int i=0; i<len; i++){
                bw.write(s.charAt(i));
                cnt+=(s.charAt(i)-'0');
            }
            if(s.charAt(len)=='e'){
                if(cnt%2==1) bw.write("1\n");
                else bw.write("0\n");
            }else{
                if(cnt%2==0) bw.write("1\n");
                else bw.write("0\n");
            }
            s=br.readLine();
        }
        bw.flush();
        bw.close();
    }
}