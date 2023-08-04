import java.io.*;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        String str = bf.readLine();
        int T = Integer.parseInt(str);
        for(int i=1; i<=T; i++)
        {
            for(int j = 1; j<=i; j++)
            {
                System.out.print("*");
            }
            System.out.println();
        }




    }
}
