import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int n = Integer.parseInt(br.readLine());
        String s;
        char a[][]=new char[n+1][n+1];
        for(int i=0; i<n; i++){
            s=br.readLine();
            for(int j=0; j<n; j++){
                a[i][j] = s.charAt(j);
            }
            a[i][n]='X';
            a[n][i]='X';
        }
        int r = 0;
        int c = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n - 1; j++) {
                r += (a[i][j] == '.' && a[i][j + 1] == '.' && a[i][j + 2] == 'X') ? 1 : 0;
                c += (a[j][i] == '.' && a[j + 1][i] == '.' && a[j + 2][i] == 'X') ? 1 : 0;
            }
        }

        bw.write(r + " " + c);
        bw.flush();
        bw.close();
    }
}
