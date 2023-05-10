// https://www.acmicpc.net/problem/13241
import java.util.*;
class Main {
	public static void main (String[] args) {
		Scanner sc = new Scanner(System.in);
		long a = sc.nextInt(), b = sc.nextInt(), gcd = gcd(a, b);
		System.out.print(a * b / gcd);
	}
	static long gcd(long a, long b) {
		return b == 0 ? a : gcd(b, a % b);
	}
}