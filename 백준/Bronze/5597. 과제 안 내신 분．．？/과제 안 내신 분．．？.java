import java.io.*;
import java.util.StringTokenizer;


public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int[] arr = new int[31];
        for(int i=0; i<28; i++){

            int N = Integer.parseInt(br.readLine());

            arr[N] = N;
        }

        for(int i=1; i<=30; i++){
            if(arr[i]==0) System.out.println(i);
        }
    }
}


