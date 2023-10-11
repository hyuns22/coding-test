import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int hour = sc.nextInt();
		int minute = sc.nextInt();
		
		if (minute>=45) {
			minute -= 45;
			System.out.println(hour+" "+minute);
			return;
		}
		
		if (hour==0) {
			hour = 23;
		}
		else hour -= 1;
		
		minute = minute+15;
		System.out.println(hour+" "+minute);
		
		sc.close();
	}
}
