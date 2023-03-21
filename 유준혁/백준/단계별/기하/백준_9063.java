// https://www.acmicpc.net/problem/9063
import java.util.*;
class Main {
	public static void main (String[] args) {
		Scanner sc = new Scanner(System.in);
		int min = -1 << 20, max = 1 << 20, xmin = max, xmax = min, ymin = max, ymax = min, n = sc.nextInt();
		while(n-->0) {
			int x = sc.nextInt(), y = sc.nextInt();
			xmin = Math.min(xmin, x);
			ymin = Math.min(ymin, y);
			xmax = Math.max(xmax, x);
			ymax = Math.max(ymax, y);
		}
		System.out.print((xmax - xmin) * (ymax - ymin));
	}
}