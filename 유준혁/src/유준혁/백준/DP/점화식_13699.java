package 유준혁.백준.DP;

import java.util.*;
public class 점화식_13699 {
	public static void main(String[] ar) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		long[] dp = new long[n + 1];
		dp[0] = 1;
		for(int i = 1; i <= n; i++) {
			for(int j = 0; j < i; j++) {
				dp[i] += dp[j] * dp[i - j - 1];
			}
		}
		System.out.println(Arrays.toString(dp));
		System.out.print(dp[n]);
	}
}
