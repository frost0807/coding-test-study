import java.util.*;
class Main {
	public static void main (String[] args) {
		Scanner sc = new Scanner(System.in);
		int x = sc.nextInt(), n = sc.nextInt();
		while(n--> 0) x -= sc.nextInt() * sc.nextInt();
		System.out.print(x == 0 ? "Yes" : "No");
	}
}