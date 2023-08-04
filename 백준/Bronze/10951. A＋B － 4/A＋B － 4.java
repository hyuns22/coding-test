import java.io.*;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        while(true)
        {
            String str = bf.readLine();
            if(str == null) break;
            StringTokenizer st = new StringTokenizer(str);
            int A = Integer.parseInt(st.nextToken());
            int B = Integer.parseInt(st.nextToken());

            if(A==0 && B==0)
            {
                break;
            }
            else
            {
                bw.write((A+B)+""+"\n");
            }

        }
        bw.close();
    }
}
