import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        Set<Integer> set = new HashSet<>();

        int n = Integer.parseInt(br.readLine());
        String s[] = br.readLine().split(" ");
        for(int i=0; i<n; i++){
            set.add(Integer.parseInt(s[i]));
        }
        List<Integer> list = new ArrayList<>(set);
        Collections.sort(list);

        for(int i : list){
            bw.write(i+" ");
        }

        bw.flush();
        bw.close();
    }
}
