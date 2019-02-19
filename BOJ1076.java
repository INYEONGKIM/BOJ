import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String s;
        long res = 0;
        for(int i=0; i<3; i++){
            s = br.readLine();
            switch (s) {
                case "black":
                    if(i==2) res*=1;
                    break;
                case "brown":
                    if(i==2)
                        res*=Math.pow(10,1);
                    else
                        res+=Math.pow(10,1-i);
                    break;
                case "red":
                    if(i==2)
                        res*=Math.pow(10,2);
                    else
                        res+=2*Math.pow(10,1-i);
                    break;
                case "orange":
                    if(i==2)
                        res*=Math.pow(10,3);
                    else
                        res+=3*Math.pow(10,1-i);
                    break;
                case "yellow":
                    if(i==2)
                        res*=Math.pow(10,4);
                    else
                        res+=4*Math.pow(10,1-i);
                    break;
                case "green":
                    if(i==2)
                        res*=Math.pow(10,5);
                    else
                        res+=5*Math.pow(10,1-i);
                    break;
                case "blue":
                    if(i==2)
                        res*=Math.pow(10,6);
                    else
                        res+=6*Math.pow(10,1-i);
                    break;
                case "violet":
                    if(i==2)
                        res*=Math.pow(10,7);
                    else
                        res+=7*Math.pow(10,1-i);
                    break;
                case "grey":
                    if(i==2)
                        res*=Math.pow(10,8);
                    else
                        res+=8*Math.pow(10,1-i);
                    break;
                case "white":
                    if(i==2)
                        res*=Math.pow(10,9);
                    else
                        res+=9*Math.pow(10,1-i);
                    break;
            }
        }
        System.out.println(res);
    }
}
