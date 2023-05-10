// https://www.acmicpc.net/problem/11478
import java.util.*;
class Main {
	public static void main (String[] args) {
		Scanner sc = new Scanner(System.in);
		String str = sc.next();
		int len = str.length();
		Set<String> set = new HashSet<>();
		for(int i = 0; i < len; i++) {
			for(int j = i + 1; j <= len; j++) {
				set.add(str.substring(i, j));
			}
		}
		System.out.print(set.size());
	}
}