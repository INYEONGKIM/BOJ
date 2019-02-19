import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int n = Integer.parseInt(br.readLine().trim());
        String s[];
        while(n-->0){
            s=br.readLine().trim().split(" ");
            switch (s[1]){
                case "kg":
                    bw.write(String.format("%.4f", Double.parseDouble(s[0])*2.2046) + " lb\n");
                    break;
                case "lb":
                    bw.write(String.format("%.4f", Double.parseDouble(s[0])*0.4536)+ " kg\n");
                    break;
                case "l":
                    bw.write(String.format("%.4f", Double.parseDouble(s[0])*0.2642)+ " g\n");
                    break;
                case "g":
                    bw.write(String.format("%.4f", Double.parseDouble(s[0])*3.7854)+ " l\n");
                    break;
            }
        }
        bw.flush();
        bw.close();
    }
}
