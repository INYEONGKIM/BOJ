import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int cnt=0,tmp,n=Integer.parseInt(br.readLine());
        double gpa=0;
        String s[];
        while(n-->0){
            s=br.readLine().split(" ");
            tmp=Integer.parseInt(s[1]);
            cnt+=tmp;
            switch (s[2]){
                case "A+":
                    gpa+=(4.3*tmp);
                    break;
                case "A0":
                    gpa+=(4.0*tmp);
                    break;
                case "A-":
                    gpa+=(3.7*tmp);
                    break;
                case "B+":
                    gpa+=(3.3*tmp);
                    break;
                case "B0":
                    gpa+=(3.0*tmp);
                    break;
                case "B-":
                    gpa+=(2.7*tmp);
                    break;
                case "C+":
                    gpa+=(2.3*tmp);
                    break;
                case "C0":
                    gpa+=(2.0*tmp);
                    break;
                case "C-":
                    gpa+=(1.7*tmp);
                    break;
                case "D+":
                    gpa+=(1.3*tmp);
                    break;
                case "D0":
                    gpa+=(1.0*tmp);
                    break;
                case "D-":
                    gpa+=(0.7*tmp);
                    break;
                case "F":
                    gpa+=(0.0*tmp);
                    break;
            }
        }
        bw.write(String.format("%.2f",gpa/cnt));
        bw.flush();
        bw.close();
    }
}
