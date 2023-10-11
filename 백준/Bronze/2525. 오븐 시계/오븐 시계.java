import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int hour = sc.nextInt();
		int minute = sc.nextInt();
		int plus = sc.nextInt();
		
		minute += plus;
		
		if(minute>=60) {
			hour += minute/60;
			minute = minute%60;
		}
		
		if(hour>=24) hour -= 24;
		
		System.out.println(hour+" "+minute);
		sc.close();
	}
}
