package test;

import java.io.*;

public class BOJ2863 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        double a,b,c,d,temp=-1,max=-1;
        String s[]=br.readLine().split(" ");
        a=Double.parseDouble(s[0]);
        b=Double.parseDouble(s[1]);
        s=br.readLine().split(" ");
        c=Double.parseDouble(s[0]);
        d=Double.parseDouble(s[1]);
        int res=-1;
        for(int i=0; i<4; i++){
            switch (i){
                case 0:
                    temp=(a/c)+(b/d);
                    break;
                case 1:
                    temp=(c/d)+(a/b);
                    break;
                case 2:
                    temp=(d/b)+(c/a);
                    break;
                case 3:
                    temp=(b/a)+(d/c);
                    break;
            }
            if(max<temp){
                max=temp;
                res=i;
            }
        }
        bw.write(res+"");
        bw.flush();
        bw.close();
    }
}