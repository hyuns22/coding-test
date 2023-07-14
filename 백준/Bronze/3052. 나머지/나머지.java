import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        int[] arr = new int[42];
        Scanner sc = new Scanner(System.in);
        for(int i=0; i<10; i++)
        {
            int temp = sc.nextInt();
            arr[temp%42] = 1;
        }
        int cnt = 0;
        for(int i=0; i<42; i++)
        {
            if(arr[i]==1)
                cnt++;
        }
        System.out.println(cnt);
    }
}
