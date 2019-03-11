import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String s[];
        int x1,x2,y1,y2,res=0;
        boolean a[][] = new boolean[100][100];
        for(int cnt=0; cnt<4; cnt++){
            s=br.readLine().split(" ");
            x1=Integer.parseInt(s[0]);
            y1=Integer.parseInt(s[1]);
            x2=Integer.parseInt(s[2]);
            y2=Integer.parseInt(s[3]);
            for(int i=x1; i<x2; i++){
                for(int j=y1; j<y2; j++){
                    a[i][j]=true;
                }
            }
        }
        for(int i=0; i<100; i++){
            for(int j=0; j<100; j++){
                if(a[i][j]) res++;
            }
        }
        bw.write(res+"");
        bw.flush();
        bw.close();
    }
}
