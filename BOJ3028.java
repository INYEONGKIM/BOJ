import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String s=br.readLine();
        byte a[]={1, 0, 0};
        byte tmp;
        char temp;
        for(int i=0;i<s.length(); i++){
            temp=s.charAt(i);
            if(temp=='A'){
              tmp=a[0];
              a[0]=a[1];
              a[1]=tmp;
            }else if(temp=='B'){
                tmp=a[1];
                a[1]=a[2];
                a[2]=tmp;
            }else{
                tmp=a[0];
                a[0]=a[2];
                a[2]=tmp;
            }
        }
        for(int i=0; i<3; i++){
            if(a[i]==1) System.out.println(i+1);
        }
    }
}
