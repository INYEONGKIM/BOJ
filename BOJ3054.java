package test;

import java.io.*;

public class BOJ3054 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String s=br.readLine();
        String top=".", sec=".", mid="#";
        int len=s.length();
        for(int i=0; i<len; i++){
            if(len%3!=2){
                if(i%3==0){
                    mid+=("."+s.charAt(i)+".#");
                }else{
                    mid+=("."+s.charAt(i)+".*");
                }
            }else{
                mid+=("."+s.charAt(i)+".");
                if(i==len-1){
                    mid+="#";
                }else{
                    if(i%3==0){
                        mid+="#";
                    }else{
                        mid+="*";
                    }
                }
            }
            if(i%3==2){
                top+=".*..";
                sec+="*.*.";
            }else{
                top+=".#..";
                sec+="#.#.";
            }
        }
        bw.write(top+"\n");
        bw.write(sec+"\n");
        bw.write(mid+"\n");
        bw.write(sec+"\n");
        bw.write(top+"\n");

        bw.flush();
        bw.close();
    }
}