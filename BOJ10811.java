import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String s[] = br.readLine().split(" ");
        int n=Integer.parseInt(s[0]), m=Integer.parseInt(s[1]);
        int a[]=new int[n+1];
        for(int i=1; i<=n; i++){
            a[i]=i;
        }
        int b,c;
        while(m-->0){
            s=br.readLine().split(" ");
            b=Integer.parseInt(s[0]);
            c=Integer.parseInt(s[1]);
            while(b<c){
                swap(a,b,c);
                b++;
                c--;
            }
        }
        for(int i=1; i<=n; i++){
            bw.write(a[i]+" ");
        }
        bw.flush();
        bw.close();
    }

    public static void swap(int a[],int b, int c){
        int temp = a[b];
        a[b]=a[c];
        a[c]=temp;
    }
}
