// https://www.acmicpc.net/problem/24416
import java.util.*;
class Main {
	static int fibo(int n) { return n <= 2 ? 1 : (fibo(n - 1) + fibo(n - 2)); }
	public static void main (String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt(), f1 = fibo(n), f2 = n - 2;
		System.out.printf("%d %d", f1, f2);
	}
}