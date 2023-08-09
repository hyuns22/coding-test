import java.io.*;
import java.util.*;



public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int n = Integer.parseInt(br.readLine());
        char[] arr = new char[n];
        arr = (br.readLine()).toCharArray();
        int sum=0;
        for(char num : arr){
            sum+=Character.getNumericValue(num);
        }
        bw.write(sum+"");
        bw.close();
    }
}



