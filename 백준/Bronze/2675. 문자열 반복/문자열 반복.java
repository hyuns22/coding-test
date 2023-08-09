import java.io.*;
import java.util.*;



public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int n = Integer.parseInt(br.readLine());
        for(int i=0;i<n;i++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            char[] arr = (st.nextToken()).toCharArray();
            for(char c : arr){
                for(int j=0; j<a; j++){
                    bw.write(c);
                }
            }
            bw.write("\n");
        }
        bw.close();
    }
}



