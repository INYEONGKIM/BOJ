import java.io.*;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int n=Integer.parseInt(br.readLine());
        Entry e[] = new Entry[n];
        for(int i=0; i<n; i++){
            e[i] = new Entry(br.readLine());
        }
        Arrays.sort(e);
        for(int i=0; i<n; i++){
            bw.write(e[i].s+"\n");
        }
        bw.flush();
        bw.close();
    }
}

class Entry implements Comparable<Entry>{
    String s;

    public Entry(String s) {
        this.s = s;
    }

    @Override
    public int compareTo(Entry o) {
        int thLen =this.s.length(), oLen = o.s.length();
        if(thLen > oLen){
            return 1;
        }else if(thLen==oLen){
            int thSum=0, oSum=0;
            for(int i=0; i<oLen; i++){
                if(this.s.charAt(i)>='0' && this.s.charAt(i)<='9') thSum+=(this.s.charAt(i)-'0');
                if(o.s.charAt(i)>='0' && o.s.charAt(i)<='9') oSum+=(o.s.charAt(i)-'0');
            }
            if(thSum > oSum){
                return 1;
            }else if(thSum==oSum){
                if(this.s.compareTo(o.s) > 0) return 1;
            }
        }
        return -1;
    }
}
