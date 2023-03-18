// https://www.acmicpc.net/problem/2559
import java.util.*;
class Main {
	public static void main (String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt(), k = sc.nextInt(), max = -1 << 30;
		int[] sum = new int[n + 1];
		for(int i = 0; i < n; i++) sum[i + 1] = sum[i] + sc.nextInt();
		for(int i = 0; i < n - k + 1; i++) max = Math.max(max, sum[i + k] - sum[i]);
		System.out.print(max);
	}
}