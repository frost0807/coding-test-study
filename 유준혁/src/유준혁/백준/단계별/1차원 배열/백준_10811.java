import java.util.*;
class Main {
	public static void main (String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt(), m = sc.nextInt();
		int[] arr = new int[n];
		for(int i = 0; i < n; i++) arr[i] = i + 1;
		while(m-->0) {
			int a = sc.nextInt() - 1, b = sc.nextInt() - 1;
			int[] temp = new int[n];
			for(int i = 0; i < n; i++) temp[i] = arr[i];
			for(int i = 0; i < b - a + 1; i++) temp[a + i] = arr[b - i];
			arr = temp;
		}
		for(int i : arr) System.out.print(i + " ");
	}
}