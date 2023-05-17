package 유준혁.백준.단계별.문자열알고리즘1;
import java.util.*;
public class 문자열집합_14425 {
    public static void main (String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt(), m = sc.nextInt(), cnt = 0;
		Set<String> set = new HashSet<>();
		while(n-->0) set.add(sc.next());
		while(m-->0) cnt += set.contains(sc.next()) ? 1 : 0;
		System.out.print(cnt);
	}
}
