import java.io.*;
import java.util.Stack;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        Stack<Integer> sl = new Stack<>();
        Stack<Integer> sr = new Stack<>();
        int n = Integer.parseInt(br.readLine().trim());
        int a[] = new int[n];
        for(int i=0; i<n; i++){
            a[i] = Integer.parseInt(br.readLine());
        }
        sl.push(a[0]);
        for(int i=1; i<n; i++){
            if(a[i]>sl.peek()) sl.push(a[i]);
        }
        sr.push(a[n-1]);
        for(int i=n-2; i>=0; i--){
            if(a[i]>sr.peek()) sr.push(a[i]);
        }
        bw.write(sl.size()+"\n"+sr.size());
        bw.flush();
        bw.close();
    }
}
