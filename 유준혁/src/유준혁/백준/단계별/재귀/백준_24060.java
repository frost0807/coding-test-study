// https://www.acmicpc.net/problem/24060
import java.util.*;
class Main {
	static int save = -1, k;
	static int[] arr, tmp;
	public static void main (String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		k = sc.nextInt();
		arr = new int[n];
		tmp = new int[n];
		for(int i = 0; i < n; i++) arr[i] = sc.nextInt();
		mergeSort(0, n - 1);
		System.out.print(save);
	}
	static void mergeSort(int s, int e) {
		if (s < e) {
			int m = (s + e) / 2;
			mergeSort(s, m);
			mergeSort(m + 1, e);

			int p = s;
			int q = m + 1;
			int idx = p;

			while (p <= m || q <= e) {
				if (q > e || (p <= m && arr[p] < arr[q])) {
					tmp[idx++] = arr[p++];
				} else {
					tmp[idx++] = arr[q++];
				}
			}

			for (int i = s; i <= e; i++) {
				k--;
				if (k == 0) save = tmp[i];
				arr[i] = tmp[i];
			}
		}
	}
}