// https://www.acmicpc.net/problem/2477
import java.util.*;
class Main {
	public static void main (String[] args) {
		Scanner sc = new Scanner(System.in);
		int k = sc.nextInt(), big = 1, small = 1;
		int[][] arr = new int[6][];
		int[] cnt = new int[6];
		for(int i = 0; i < 6; i++) {
			int[] a = new int[] { sc.nextInt(), sc.nextInt() };
			arr[i] = a;
			cnt[a[0]]++;
		}
		for(int i = 0; i < 6; i++) {
			int[] a = arr[i];
			if (cnt[a[0]] == 1) big *= a[1];
			else {
				int n = (i + 1) % 6, m = (i + 2) % 6;
				if(a[0] == arr[m][0]) small *= arr[n][1];
			}
		}
		System.out.print((big - small) * k);
	}
}