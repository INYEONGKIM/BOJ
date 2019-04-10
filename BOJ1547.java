import java.io.*;

public class Main {
    static int a[]=new int[3];

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String s[];
        int n=Integer.parseInt(br.readLine());
        a[0] = 1;
        while(n-->0){
            s=br.readLine().split(" ");
            swap(Integer.parseInt(s[0])-1, Integer.parseInt(s[1])-1);
        }
        for(int i=0; i<3; i++){
            if(a[i]==1){
                bw.write(i+1+"");
                break;
            }
        }
        bw.flush();
        bw.close();
    }
    public static void swap(int b, int c){
        int temp=a[b];
        a[b]=a[c];
        a[c]=temp;
    }
}
