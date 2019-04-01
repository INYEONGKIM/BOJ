import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String s[] = br.readLine().split(" ");
        int e=Integer.parseInt(s[0])+Integer.parseInt(s[1]), c=Integer.parseInt(s[2]), res=0, temp;
        while(e>=c){
            temp = e/c;
            res += temp;
            e = e%c + temp;
        }
        bw.write(res+"");
        bw.flush();
        bw.close();
    }
}
