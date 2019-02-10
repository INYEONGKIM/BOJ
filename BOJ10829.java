import java.io.*;
import java.util.Stack;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        Stack<Long> stk = new Stack<>();
        long x=Long.parseLong(br.readLine());
        while(x>0){
            stk.push(x%2);
            x/=2;
        }
        while(!stk.isEmpty()){
            bw.write(stk.pop()+"");
        }
        bw.flush();
        bw.close();
    }
}
