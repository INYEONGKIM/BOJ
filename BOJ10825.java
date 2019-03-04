import java.io.*;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int n=Integer.parseInt(br.readLine());
        Entry e[] = new Entry[n];
        String s[];
        for(int i=0; i<n; i++){
            s=br.readLine().split(" ");
            e[i]=new Entry(s[0], Integer.parseInt(s[1]), Integer.parseInt(s[2]), Integer.parseInt(s[3]));
        }
        Arrays.sort(e);
        for(int i=0; i<e.length; i++){
            bw.write(e[i].name+"\n");
        }
        bw.flush();
        bw.close();
    }
}

class Entry implements Comparable<Entry>{
    String name;
    int kor,eng,math;

    public Entry(String name, int kor, int eng, int math) {
        this.name = name;
        this.kor = kor;
        this.eng = eng;
        this.math = math;
    }

    @Override
    public int compareTo(Entry e) {
        if(this.kor<e.kor){
            return 1;
        }else if(this.kor==e.kor){
            if(this.eng>e.eng){
                return 1;
            }else if(this.eng==e.eng){
                if(this.math<e.math){
                    return 1;
                }else if(this.math==e.math){
                    if(this.name.compareTo(e.name)>0){
                        return 1;
                    }
                }
            }
        }
        return -1;
    }
}
