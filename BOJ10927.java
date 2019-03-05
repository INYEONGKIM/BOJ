import java.io.*;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String s=br.readLine();
        bw.write(encodeSHA512(s));

        bw.flush();
        bw.close();
    }

    public static String encodeSHA512(String pswd) {
        MessageDigest md;
        String tempPassword = "";
        try {
            md = MessageDigest.getInstance("MD5");
            md.update(pswd.getBytes());
            byte[] mb = md.digest();
            for (int i = 0; i < mb.length; i++) {
                byte temp = mb[i];
                String s = Integer.toHexString(new Byte(temp));
                while (s.length() < 2) {
                    s = "0" + s;
                }
                s = s.substring(s.length() - 2);
                tempPassword += s;
            }

        } catch (NoSuchAlgorithmException e) {
            return tempPassword;
        }
        return tempPassword;
    }

}
