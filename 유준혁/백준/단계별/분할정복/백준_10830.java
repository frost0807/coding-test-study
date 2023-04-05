import java.util.*;
class Main {
	static int[][] arr, rst;
	static int[][] pow(int[][] arr, long m) {
		if(m == 1) return arr;
		int[][] tmp = pow(arr, m / 2);
		tmp = mul(tmp, tmp);
		if(m % 2 == 0) return tmp;
		else return mul(tmp, arr);
	}
	static int[][] mul(int[][] a, int[][] b) {
		int n = a.length;
		int[][] r = new int[n][n];
		for(int i = 0; i < n; i++) {
			for(int j = 0; j < n; j++) {
				for(int k = 0; k < n; k++) r[i][j] += a[i][k] * b[k][j];
				r[i][j] %= 1000;
			}
		}
		return r;
	}
	public static void main (String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		long m = sc.nextLong();
		arr = new int[n][n];
		for(int i = 0; i < n; i++) {
			for(int j = 0; j < n; j++) {
				arr[i][j] = sc.nextInt() % 1000;
			}
		}
		rst = pow(arr, m);
		for(int[] r : rst) {
			for(int i : r) System.out.print(i + " ");
			System.out.println();
		}
	}
}