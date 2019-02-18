import java.io.*;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        System.out.printf("%.0f", (Math.pow(Integer.parseInt(st.nextToken()),2) +Math.pow(Integer.parseInt(st.nextToken()),2)
                + Math.pow(Integer.parseInt(st.nextToken()),2) + Math.pow(Integer.parseInt(st.nextToken()),2)
                + Math.pow(Integer.parseInt(st.nextToken()),2))%10);
    }
}
