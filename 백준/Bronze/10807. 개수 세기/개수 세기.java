import java.io.*;
import java.util.StringTokenizer;


public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int N = Integer.parseInt(br.readLine());
        String str = br.readLine();
        StringTokenizer st = new StringTokenizer(str);

        int v = Integer.parseInt(br.readLine());

        int[] arr = new int[N];

        int cnt = 0;

        for(int i=0; i<N; i++)
        {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        for(int i=0; i<N; i++)
        {
            if(arr[i]==v) cnt++;
        }

        bw.write(cnt+"");
        bw.close();
    }
}


