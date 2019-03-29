import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n=Integer.parseInt(br.readLine());
        int a[]=new int[n];
        int i,d=0;
        boolean flag = true;
        for(i=0; i<n; i++){
            a[i] = Integer.parseInt(br.readLine());
            if(i==1){
                d = a[1]-a[0];
            }else if(i>1){
                if(a[i] != a[i-1]+d){
                    flag=false;
                }
            }
        }
        if(flag)
            System.out.println(a[n-1]+d);
        else
            System.out.println(String.format("%.0f",a[0]*Math.pow((a[1]/a[0]), n)));
    }
}
