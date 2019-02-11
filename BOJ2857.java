import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int cnt=0, flag;
        String s;
        for(int i=1; i<6; i++){
            s=br.readLine();
            if(s.length()>=3){
                if(s.charAt(0)=='F' && s.charAt(1)=='B'){
                    flag=2;
                }else if(s.charAt(1)=='F'){
                    flag=1;
                }else{
                    flag=0;
                }

                for(int j=2; j<s.length(); j++){
                    if(flag==2){
                        if(s.charAt(j)=='I'){
                            cnt++;
                            bw.write(i+" ");
                            break;
                        }else{
                            flag=0;
                        }
                    }else if(flag==1){
                        if(s.charAt(j)=='B')
                            flag=2;
                        else
                            flag=0;
                    }else{
                        if(s.charAt(j)=='F') flag=1;
                    }
                }
            }
        }
        if(cnt==0) bw.write("HE GOT AWAY!");
        bw.flush();
        bw.close();
    }
}
