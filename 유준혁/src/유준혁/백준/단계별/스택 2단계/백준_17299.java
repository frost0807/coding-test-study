// https://www.acmicpc.net/problem/17299
import java.util.*;
class Main {
	public static void main (String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int[] arr = new int[n], cnt = new int[1000001];
		String[] rst = new String[n];
		Arrays.fill(rst, "-1");
		Stack<Integer> stack = new Stack<>();
		for(int i = 0; i < n; i++) cnt[arr[i] = sc.nextInt()]++;
		for(int i = 0; i < n; i++) {
			while(!stack.isEmpty() && cnt[arr[stack.peek()]] < cnt[arr[i]]) rst[stack.pop()] = arr[i] + "";
			stack.push(i);
		}
		System.out.print(String.join(" ", rst));
	}
}