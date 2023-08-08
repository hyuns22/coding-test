import java.io.*;
import java.util.*;


public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        Set<Integer> set1 = new HashSet<>();
        for(int i=0; i<10;i++){
            int N = Integer.parseInt(br.readLine());
            set1.add(N % 42);
        }

        bw.write(set1.size()+"");
        bw.close();
    }
}