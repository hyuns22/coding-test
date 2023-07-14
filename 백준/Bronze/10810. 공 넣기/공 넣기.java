import javax.swing.plaf.synth.SynthOptionPaneUI;
import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N, M;
        N = sc.nextInt();
        M = sc.nextInt();
        int[] array=new int[N+1];

        for(int i =0; i<M; i++)
        {
            int x,y,z;
            x= sc.nextInt();
            y= sc.nextInt();
            z= sc.nextInt();
            for(int j=x; j<=y; j++)
            {
                array[j] = z;
            }
        }
        for(int i=1; i<N+1; i++)
        {
            System.out.print(array[i]+" ");
        }
    }
}
