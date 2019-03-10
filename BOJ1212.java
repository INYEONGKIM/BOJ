import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String s=br.readLine();
        int size=s.length();
        switch (s.charAt(0)-'0'){
            case 0:
                bw.write("0");
                break;
            case 1:
                bw.write("1");
                break;
            case 2:
                bw.write("10");
                break;
            case 3:
                bw.write("11");
                break;
            case 4:
                bw.write("100");
                break;
            case 5:
                bw.write("101");
                break;
            case 6:
                bw.write("110");
                break;
            case 7:
                bw.write("111");
                break;
        }

        for(int i=1; i<size; i++){
            switch (s.charAt(i)-'0'){
                case 0:
                    bw.write("000");
                    break;
                case 1:
                    bw.write("001");
                    break;
                case 2:
                    bw.write("010");
                    break;
                case 3:
                    bw.write("011");
                    break;
                case 4:
                    bw.write("100");
                    break;
                case 5:
                    bw.write("101");
                    break;
                case 6:
                    bw.write("110");
                    break;
                case 7:
                    bw.write("111");
                    break;
            }
        }
        bw.flush();
        bw.close();
    }
}
