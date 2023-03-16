import java.util.*;
class Main {
	public static void main (String[] args) {
		Scanner sc = new Scanner(System.in);
		int i = 0, j = 0, max = 0;
		for(int k = 0; k < 81; k++) {
			int x = sc.nextInt();
			if (max < x) {
				max = x;
				i = k / 9;
				j = k % 9;
			}
		}
		System.out.printf("%d\n%d %d", max, i + 1, j + 1);
	}
}