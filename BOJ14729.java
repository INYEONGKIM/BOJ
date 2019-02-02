import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        double a[] = new double[Integer.parseInt(br.readLine())];

        for (int i=0; i<a.length; i++)
            a[i] = Double.parseDouble(br.readLine());
        Arrays.sort(a);
        for (int i=0; i<7; i++)
            System.out.printf("%.3f\n", a[i]);

    }
}
