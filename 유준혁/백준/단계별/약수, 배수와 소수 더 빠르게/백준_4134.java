// https://www.acmicpc.net/problem/4134
import java.util.*;
class Main {
	public static void main (String[] args) {
		Scanner sc = new Scanner(System.in);
		int tc = sc.nextInt();
		while(tc-->0) {
			long n = Math.max(sc.nextLong(), 2);
			while(!isPrime(n)) n++;
			System.out.println(n);
		}
	}
	static boolean isPrime(long n) {
		for(long i = 2; i <= Math.sqrt(n); i++) if (n % i == 0) return false;
		return true;
	}
}