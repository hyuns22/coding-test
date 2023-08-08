import java.io.*;
import java.util.*;

import static java.util.Arrays.stream;


public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int N = Integer.parseInt(br.readLine());

        List<Integer> arr = new ArrayList<>();
        StringTokenizer st = new StringTokenizer(br.readLine());
        for(int i=0; i<N;i++){
            arr.add(Integer.parseInt(st.nextToken()));
        }
        int max = Collections.max(arr);
        double sum =0;
        for(int grade:arr){
            sum+=(double)grade/max*100;
        }
        System.out.println(sum/N);
    }
}


