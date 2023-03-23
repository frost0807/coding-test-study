// https://www.acmicpc.net/problem/25682
// 체스판 다시 칠하기 누적합 버전
import java.util.*;
class Main {
	public static void main (String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt(), m = sc.nextInt(), k = sc.nextInt(), min = k * k;
		int[][] cnt = new int[n + 1][m + 1];
		for(int i = 0; i < n; i++) {
			char[] arr = sc.next().toCharArray();
			for(int j = 0; j < m; j++) {
				int c = (arr[j] == 'B' && (i + j) % 2 == 1) || (arr[j] == 'W' && (i + j) % 2 == 0) ? 1 : 0;
				cnt[i+1][j + 1] = cnt[i+1][j] + cnt[i][j+1] - cnt[i][j] + c;
			}
		}   
		for(int i = k; i <= n; i++) {
			for(int j = k; j <= m; j++) {
				int c = cnt[i][j] + cnt[i-k][j-k] - cnt[i-k][j] - cnt[i][j-k];
				min = Math.min(min, Math.min(k * k - c, c));
			}
		}
		System.out.print(min);
	}
}