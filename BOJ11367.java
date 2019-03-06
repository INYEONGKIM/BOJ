import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int n=Integer.parseInt(br.readLine());
        String s[];
        int grade;
        while(n-->0){
            s=br.readLine().split(" ");
            bw.write(s[0]+" ");
            grade=Integer.parseInt(s[1]);
            if(grade>=97){
                bw.write("A+\n");
            }else if(grade>=90){
                bw.write("A\n");
            }else if(grade>=87){
                bw.write("B+\n");
            }else if(grade>=80){
                bw.write("B\n");
            }else if(grade>=77){
                bw.write("C+\n");
            }else if(grade>=70){
                bw.write("C\n");
            }else if(grade>=67){
                bw.write("D+\n");
            }else if(grade>=60){
                bw.write("D\n");
            }else{
                bw.write("F\n");
            }
        }
        bw.flush();
        bw.close();
    }
}
