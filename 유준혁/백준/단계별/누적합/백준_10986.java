import java.util.*;
class Main {
	public static void main (String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt(), m = sc.nextInt();
		long[] cnt = new long[m], sum = new long[n + 1];
		for(int i = 0; i < n; i++) {
			int x = sc.nextInt();
			sum[i + 1] = (sum[i] + x) % m;
			cnt[(int)sum[i + 1]]++;
		}
		long rst = cnt[0];
		for(long i : cnt) rst += i * (i - 1) / 2;
		System.out.print(rst);
	}
}