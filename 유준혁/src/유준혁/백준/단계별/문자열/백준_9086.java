import java.util.*;
class Main {
	public static void main (String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		while(n-->0) {
			String str = sc.next();
			System.out.println(str.charAt(0) + "" + str.charAt(str.length() - 1));
		}
	}
}