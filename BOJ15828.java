import java.io.*;
import java.util.LinkedList;
import java.util.Queue;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int p,n=Integer.parseInt(br.readLine());
        Queue<Integer> q = new LinkedList<>();
        while(true){
            p=Integer.parseInt(br.readLine());
            if(p==-1) break;
            if(p==0){
                q.poll();
            }else if(q.size()<n){
                q.offer(p);
            }
        }
        if(q.isEmpty()){
            bw.write("empty");
        }else {
            while (!q.isEmpty()) {
                bw.write(q.poll()+" ");
            }
        }
        bw.flush();
        bw.close();
    }
}
