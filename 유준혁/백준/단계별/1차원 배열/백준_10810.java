import java.util.*;
class Main {
	public static void main (String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt(), m = sc.nextInt();
		int[] arr = new int[n];
		while(m-->0) {
		    int i = sc.nextInt(), j = sc.nextInt(), k = sc.nextInt();
		    for(int x = i - 1; x < j; x++) arr[x] = k;
		}
		for(int i : arr) System.out.print(i + " ");
	}
}