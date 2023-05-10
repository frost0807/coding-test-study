import java.util.*;
class Main {
	public static void main (String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int[] cnt = new int[300];
		while(n--> 0) cnt[sc.nextInt() + 100]++;
		System.out.print(cnt[sc.nextInt() + 100]);
	}
}