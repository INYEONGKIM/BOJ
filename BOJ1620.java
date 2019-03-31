import java.io.*;
import java.util.HashMap;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String s1,s[]=br.readLine().split(" ");
        int n = Integer.parseInt(s[0]);
        int m = Integer.parseInt(s[1]);
        HashMap<String, Integer> map =  new HashMap<>();
        String arr[] = new String[n];

        for(int i=0; i<n; i++){
            s1 = br.readLine();
            arr[i] = s1;
            map.put(s1, i+1);
        }
        for(int i=0; i<m; i++){
            s1 = br.readLine();
            if (s1.charAt(0)>='A'){
                bw.write(map.get(s1)+"\n");
            }else{
                bw.write(arr[Integer.parseInt(s1)-1]+"\n");
            }

        }
        bw.flush();
        bw.close();
    }
}
