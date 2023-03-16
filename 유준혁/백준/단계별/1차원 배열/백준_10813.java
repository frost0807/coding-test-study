import java.util.*;
class Main {
	public static void main (String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt(), m = sc.nextInt();
		int[] arr = new int[n];
		for(int i = 0; i < n; i++) arr[i] = i + 1;
		while(m-->0) {
			int a = sc.nextInt() - 1, b = sc.nextInt() - 1, t = arr[a];
			arr[a] = arr[b];
			arr[b] = t;
		}
		for(int i : arr) System.out.print(i + " ");
	}
}