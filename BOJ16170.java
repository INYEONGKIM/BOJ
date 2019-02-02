import java.io.*;
import java.text.DateFormat;
import java.text.SimpleDateFormat;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        TimeZone time = TimeZone.getTimeZone("Etc/GMT+0");
        Date today = new Date();
        DateFormat df = new SimpleDateFormat("yyyy");
        df.setTimeZone(time);
        bw.write(df.format(today)+"\n");

        DateFormat df1 = new SimpleDateFormat("MM");
        df1.setTimeZone(time);
        bw.write(df1.format(today)+"\n");

        DateFormat df2 = new SimpleDateFormat("dd");
        df2.setTimeZone(time);
        bw.write(df2.format(today)+"\n");
        
        bw.flush();
        bw.close();
    }
}
