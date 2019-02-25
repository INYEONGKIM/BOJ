import java.io.*;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String s[];
        int n = Integer.parseInt(br.readLine());
        while(n-->0){
            int n2 = Integer.parseInt(br.readLine());
            Entry e[] = new Entry[n2];
            for(int i=0; i<n2; i++){
                s=br.readLine().trim().split(" ");
                e[i] = new Entry(s[0], Integer.parseInt(s[1]));
            }
            Arrays.sort(e);
            bw.write(e[0].name+"\n");
        }
        bw.flush();
        bw.close();
    }
} //main

class Entry implements Comparable<Entry>{
    String name;
    int n;

    public Entry(String name, int n) {
        this.name = name;
        this.n = n;
    }

    @Override
    public int compareTo(Entry e) {
        return (n<e.n) ? 1 : -1;
    }
}
