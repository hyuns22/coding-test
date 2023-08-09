import java.io.*;
import java.util.*;



public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String str = (br.readLine());
        String[] st = str.split("");
        int n = Integer.parseInt(br.readLine());
        System.out.println(st[n-1]);

    }
}



