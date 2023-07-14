import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int[] arr = new int[N];
        for(int i=0; i< arr.length;i++)
        {
            arr[i] = sc.nextInt();
        }
        int mx = Arrays.stream(arr).max().getAsInt();
        
        double sum = 0;
        for(int i=0; i< arr.length; i++)
        {
            sum += (double)arr[i] / mx * 100;
        }
        System.out.println(sum/N);
    }
}
