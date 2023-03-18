// https://www.acmicpc.net/problem/10812
// 단순 구현 문제
// 은근 구현 개귀찮았음
import java.util.*;
class Main {
	public static void main (String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt(), t = sc.nextInt();
		int[] arr = new int[n + 1];
		for(int i = 0; i <= n; i++) arr[i] = i;
		while(t-->0) {
			int s = sc.nextInt(), e = sc.nextInt(), m = sc.nextInt(), len = e - s + 1;
			int[] tmp = new int[len];
			for(int i = m; i <= e; i++) tmp[i - m] = arr[i];
			for(int i = s; i < m; i++) tmp[i - s + (e - m) + 1] = arr[i];
			for(int i = s; i <= e; i++) arr[i] = tmp[i - s];
		}
		for(int i = 1; i <= n; i++) System.out.print(arr[i] + " ");
	}
}