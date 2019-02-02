package BOJ;

import java.io.*;
import java.util.*;

public class BOJ14911 {
    public static void main(String[] args) throws IOException {
        Set<Integer> hs = new HashSet<>();
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int cnt = 0;

        String[] s = br.readLine().split(" ");
        int A[] =  new int[s.length];
        for(int i=0; i<A.length; i++){
            A[i] = Integer.parseInt(s[i]);
        }

        int k = Integer.parseInt(br.readLine());


        for(int i=0; i<A.length-1; i++){
            for(int j=i+1; j<A.length; j++){
                if(A[i] + A[j] == k){
                    hs.add(A[i]);
                }
            }
        }

        List<Integer> lst = new ArrayList<>(hs);
        Collections.sort(lst);
        Iterator<Integer> iter = lst.iterator();
        while(iter.hasNext()){
            Integer e = iter.next();
            bw.write(e + " " + (k-e) +"\n");
            cnt++;
        }

        bw.write(cnt +"\n");

        bw.flush();
        bw.close();
    }
}
