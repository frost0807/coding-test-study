import java.util.*;
class Main {
	public static void main (String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt(), m = sc.nextInt();
		int[][] arr = new int[n][m];
		for(int k = 0; k < 2; k++) {
			for(int i = 0; i < n; i++) {
				for(int j = 0; j < m; j++) {
					arr[i][j] += sc.nextInt();
				}
			}
		}
		for(int[] a : arr) {
			for(int i : a) System.out.print(i + " ");
			System.out.println();
		}
	}
}