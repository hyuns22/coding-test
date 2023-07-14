import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int arr[] = new int[26];
        for (int i=0; i<26; i++)
        {
            arr[i] = -1;
        }
        char[] strin = sc.next().toCharArray();
        for (int i=0; i< strin.length;i++)
        {
            if(arr[(int)strin[i]-97]!=-1)
            continue;
            else
            {
                arr[(int)strin[i]-97] = i;
            }
        }
        for(int i=0; i<26; i++)
        {
            System.out.print(arr[i]+" ");
        }

    }
}
