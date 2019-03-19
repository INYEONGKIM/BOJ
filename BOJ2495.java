package test;

import java.io.*;

public class BOJ2495 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String s;
        char temp;
        int cnt,res;
        for(int j=0; j<3; j++){
            cnt=1;
            res=0;
            s=br.readLine();
            temp=s.charAt(0);
            for(int i=1; i<8; i++){
                if(temp==s.charAt(i)){
                    cnt++;
                }else{
                    temp=s.charAt(i);
                    if(cnt>=res){
                        res=cnt;
                        cnt=1;
                    }

                }
            }
            if(cnt>res) res=cnt;
            bw.write(res+"\n");
        }
        bw.flush();
        bw.close();
    }
}