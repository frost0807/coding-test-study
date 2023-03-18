// https://www.acmicpc.net/problem/2587
import java.util.*;
class Main {
	public static void main (String[] args) {
		Scanner sc = new Scanner(System.in);
		int sum = 0;
		int[] arr = new int[5];
		for(int i = 0; i < 5; i++) sum += arr[i] = sc.nextInt();
		Arrays.sort(arr);
		System.out.printf("%d\n%d", sum / 5, arr[2]);
	}
}