import java.io.*;
import java.util.*;


public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        List<Integer> arr = new ArrayList<>();
        int N, M;
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        for(int i=0; i<=N; i++){
            arr.add(i);
        }

        for(int i=0; i<M; i++){
            st = new StringTokenizer(br.readLine());
            int a,b;
            a = Integer.parseInt(st.nextToken());
            b = Integer.parseInt(st.nextToken());

            List<Integer> temp_arr = new ArrayList<>();
            for(int j=b; j>=a; j--){
                temp_arr.add(arr.get(j));
            }
            int cnt=0;
            for(int j=a; j<=b; j++, cnt++){
                arr.set(j, temp_arr.get(cnt));
            }
        }

        for(int i=1; i<=N; i++){
            bw.write(arr.get(i)+""+" ");
        }
        bw.close();

    }
}


