package test;

import java.io.*;

public class BOJ15921 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int n=Integer.parseInt(br.readLine());
        int a[]=new int[n];
        if(n==0){
            bw.write("divide by zero");
        }else{
            double ex=0;
            int sum=0;
            String s[]=br.readLine().split(" ");
            for(int i=0; i<n; i++){
                a[i]=Integer.parseInt(s[i]);
                sum+=a[i];
                ex+=a[i]*((double)1/n);
            }
            if(ex==0)
                bw.write("divide by zero");
            else
                bw.write(String.format("%.2f", ((double) sum/n)/ex));
        }
        bw.flush();
        bw.close();
    }
}