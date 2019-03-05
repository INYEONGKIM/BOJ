import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String s[]=br.readLine().split(" ");
        int s1=Integer.parseInt(s[0]);
        int s2=Integer.parseInt(s[1]);
        int s3=Integer.parseInt(s[2]);
        int a[]=new int[81];

        for(int i=1; i<=s1; i++){
            for(int j=1; j<=s2; j++){
                for(int k=1; k<=s3; k++){
                    a[i+j+k]++;
                }
            }
        }
        int max=0, idx=0;
        for(int i=1; i<=80; i++){
            if(a[i]>max){
                max=a[i];
                idx=i;
            }
        }
        System.out.println(idx);
    }
}
