package test;

import java.io.*;
import java.util.HashSet;
import java.util.Set;

public class BOJ1269 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String s[]=br.readLine().split(" ");
        int a=Integer.parseInt(s[0]);
        int b=Integer.parseInt(s[1]);
        int tot=a+b;
        Set<Integer> set=new HashSet<>();
        s=br.readLine().split(" ");
        for(int i=0; i<a; i++){
            set.add(Integer.parseInt(s[i]));
        }
        s=br.readLine().split(" ");
        for(int i=0; i<b; i++){
            set.add(Integer.parseInt(s[i]));
        }
        int size=set.size();
        bw.write(tot-2*(tot-size)+"");
        bw.flush();
        bw.close();
    }
}