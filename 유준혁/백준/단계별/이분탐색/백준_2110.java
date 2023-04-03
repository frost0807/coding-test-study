// https://www.acmicpc.net/problem/2110
import java.util.*;
class Main {
	public static void main (String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt(), k = sc.nextInt(), max = 0, l = 0, r = 1 << 30;
		int[] arr = new int[n];
		for(int i = 0; i < n; i++) arr[i] = sc.nextInt();
		Arrays.sort(arr);
		while(l < r) {
			int mid = (l + r) / 2, cnt = 1, last = arr[0];
			for(int i : arr) {
				if (i - last >= mid) {
					last = i;
					cnt++;
				}
			}
			if (cnt >= k) {
				l = mid + 1;
				max = Math.max(max, mid);
			} else {
				r = mid;
			}
		}
		System.out.print(max);
	}
}