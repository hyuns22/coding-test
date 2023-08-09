import java.io.*;
import java.util.*;



public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String[] arr = (br.readLine()).trim().split(" ");
        if(arr[0].equals("")) System.out.println(0);
        else System.out.println(arr.length);
    }
}



