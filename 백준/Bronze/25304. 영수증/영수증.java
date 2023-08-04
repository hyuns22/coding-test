import java.math.BigInteger;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int X, N;
        X = sc.nextInt();
        N = sc.nextInt();
        int sum = 0;
        for(int i=0; i<N; i++)
        {
            int a,b;
            a= sc.nextInt();
            b= sc.nextInt();
            sum += a*b;
        }

        if(X==sum) System.out.println("Yes");
        else System.out.println("No");

    }
}
