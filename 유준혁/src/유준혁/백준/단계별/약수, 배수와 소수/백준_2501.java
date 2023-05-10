// https://www.acmicpc.net/problem/2501
// 설명은 필요 없음
import java.util.*;
class Main {
	public static void main (String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt(), k = sc.nextInt(), v = 0;
		for(int i = 1; i <= n; i++) {
			if(n % i == 0) k--;
			if(k == 0 && v == 0)v = i;
		}
		System.out.print(v);
	}
}