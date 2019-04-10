import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int n=Integer.parseInt(br.readLine());
        String s = br.readLine();
        int len = s.length();
        int idx=0, col=len/n;
        char a[][]=new char[col][n];
        for(int i=0; i<col; i++){
            if(i%2==0){
                for(int j=0; j<n; j++){
                    a[i][j] = s.charAt(idx++);
                }
            }else{
                for(int j=n-1; j>=0; j--){
                    a[i][j] = s.charAt(idx++);
                }
            }
        }
        for(int i=0; i<n; i++){
            for(int j=0; j<col; j++){
                bw.write(a[j][i]);
            }
        }
        bw.flush();
        bw.close();
    }
}
