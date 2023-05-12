package 유준혁.백준.애드혹;
import java.util.*;
public class 비밀번호_변경_14254 {
	// 실패함
	public static void main (String[] args) {
		Scanner sc = new Scanner(System.in);
		char[] arr = sc.next().toCharArray();
		int n = arr.length, k = sc.nextInt(), c = n - k;
		int[][] cnt = new int[c][26];
		int[] max = new int[c];
		if (k <= n / 2) {
			int tmp = 0;
			for(int i = 0; i < k; i++) tmp += arr[i] != arr[i + k] ? 1 : 0;
			System.out.print(tmp);
		} else if (k == n) {
			System.out.print(0);
		} else {
			for(int i = 0; i < n; i++) {
				max[i % c] = Math.max(max[i % c], ++cnt[i % c][arr[i] - 'a']);
			}
			for(int i : max) n -= i;
			System.out.print(n);
		}
	}
}
