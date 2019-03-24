import java.io.*;
import java.util.Comparator;
import java.util.PriorityQueue;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PriorityQueue<Integer> q = new PriorityQueue<>(new Comparator<Integer>() {
            @Override
            public int compare(Integer o1, Integer o2) {
                return o2-o1;
            }
        });
        StringBuilder sb = new StringBuilder();
        int n=Integer.parseInt(br.readLine());
        int x;
        while(n-->0){
            x=Integer.parseInt(br.readLine());
            if(x==0){
                if(q.isEmpty())
                    sb.append("0\n");
                else
                    sb.append(q.poll()+"\n");
            }else {
                q.offer(x);
            }
        }
        System.out.print(sb);
    }
}
