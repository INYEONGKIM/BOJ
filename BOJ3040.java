import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int sum=0;
        int a[]=new int[9];
        boolean flag=false;
        for(int i=0; i<9; i++){
            a[i]=Integer.parseInt(br.readLine());
            sum+=a[i];
        }
        for(int i=0; i<8; i++){
            for(int j=i+1; j<9; j++){
                if((sum-(a[i]+a[j]))==100){
                    a[i]=0;
                    a[j]=0;
                    flag=true;
                    break;
                }
            }
            if(flag) break;
        }
        for(int i=0; i<9; i++){
            if(a[i]!=0) bw.write(a[i]+"\n");
        }
        bw.flush();
        bw.close();
    }
}
