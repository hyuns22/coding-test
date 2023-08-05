import java.io.*;
import java.util.StringTokenizer;


public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int N = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] arr = new int[N];

        for(int i=0;i<N;i++){
            arr[i] = Integer.parseInt(st.nextToken());
        }

        int min = arr[0];
        int max = arr[0];

        for(int i=0;i<N;i++){
            if(arr[i]>max) max = arr[i];
            if(arr[i]<min) min = arr[i];
        }

        bw.write(min+""+" "+max+"");
        bw.close();
    }

}


