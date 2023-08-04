import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int A;
        String B;
        A = sc.nextInt();
        sc.nextLine();
        B = sc.nextLine();
        System.out.println(A*((int)B.charAt(2)-48));
        System.out.println(A*((int)B.charAt(1)-48));
        System.out.println(A*((int)B.charAt(0)-48));
        System.out.println(A*Integer.parseInt(B));


    }
}
