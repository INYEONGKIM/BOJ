import java.io.*;
import java.util.ArrayDeque;
import java.util.Deque;

public class Main {
    public static void main(String[] args) throws IOException {
        Deque<Integer> dq = new ArrayDeque<>();
        BufferedReader br =  new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        String s[];
        while(n-->0){
            s = br.readLine().trim().split(" ");
            switch (s[0]){
                case "push_front":
                    dq.addFirst(Integer.parseInt(s[1]));
                    break;
                case "push_back":
                    dq.addLast(Integer.parseInt(s[1]));
                    break;
                case "pop_front":
                    if(!dq.isEmpty())
                        System.out.println(dq.removeFirst());
                    else
                        System.out.println(-1);
                    break;
                case "pop_back":
                    if(!dq.isEmpty())
                        System.out.println(dq.removeLast());
                    else
                        System.out.println(-1);
                    break;
                case "size":
                    System.out.println(dq.size());
                    break;
                case "empty":
                    if(dq.isEmpty())
                        System.out.println(1);
                    else
                        System.out.println(0);
                    break;
                case "front":
                    if(!dq.isEmpty())
                        System.out.println(dq.getFirst());
                    else
                        System.out.println(-1);
                    break;
                case "back":
                    if(!dq.isEmpty())
                        System.out.println(dq.getLast());
                    else
                        System.out.println(-1);
                    break;
            }
        }
    }
}
