import java.util.*;
class Main {
	public static void main (String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt(), idx = 0;
		int[] dis = new int[n - 1], amount = new int[n];
		for(int i = 0; i < n - 1; i++) dis[i] = sc.nextInt();
		for(int i = 0; i < n; i++) amount[i] = sc.nextInt();
		long sum = 0, min = amount[idx];
		while(idx < n - 1) {
			min = Math.min(min, amount[(int)idx]);
			sum += min * dis[(int)idx++];
		}
		System.out.print(sum);
	}
}