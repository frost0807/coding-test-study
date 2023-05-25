package 유준혁.백준.클래스;

class Maker {
	public static char[][] sdoku = new char[9][];
	public static boolean[][] X = new boolean[9][10], Y = new boolean[9][10], AREA = new boolean[9][10];
	public static boolean isEnd = false, isFail = false;
	public static int cnt = 0;
	public Maker(char[][] arr) {
		sdoku = arr;
		for(int i = 0; i < 9; i++) {
			for(int j = 0; j < 9; j++) {
				int v = sdoku[i][j] - '0';
				if (v != 0) {
					isFail = isFail | X[i][v] | Y[j][v] | AREA[getArea(i, j)][v];
					X[i][v] = true;
					Y[j][v] = true;
					AREA[getArea(i, j)][v] = true;
				}
			}
		}
	}
	static int getArea(int i, int j) {
		return (i / 3) * 3 + j / 3;
	}
	static boolean solve(int n) {
		if (isEnd) return false;
		cnt++;
		if (n == 81) {
			isEnd = true;
			return false;
		}
		int x = n / 9, y = n % 9;
		if (sdoku[x][y] == '0') {
			for(int i = 1; i <= 9; i++) {
				if (!X[x][i] && !Y[y][i] && !AREA[getArea(x, y)][i]) {
					X[x][i] = Y[y][i] = AREA[getArea(x, y)][i] = true;
					sdoku[x][y] = (char)('0' + i);
					if (solve(n + 1)) return true;
					X[x][i] = Y[y][i] = AREA[getArea(x, y)][i] = false;
					sdoku[x][y] = '0';
				}
			}
		} else {
			return solve(n + 1);
		}
		return false;
	}
}
public class 가장_오래걸리는_스도쿠_12095 {
	static boolean isEnd = false;
	static char[][] map = new char[9][9];
	static void dfs(int n) {
		if (isEnd) return;
		if (n == 81) {
			Maker maker = new Maker(map);
            StringBuilder sb = new StringBuilder();
            for(char[] arr : map) for(char c : arr) sb.append(c);
            System.out.println(sb);
			if (!maker.isFail) {
				maker.solve(0);
                System.out.println(maker.isEnd + ", " + maker.cnt);
				if (maker.isEnd && maker.cnt >= 100000) {
					isEnd = true;
					for(char[] arr : maker.sdoku) {
						for(char c : arr) System.out.print(c + " ");
						System.out.println();
					}
				}
			}
		} else {
			int x = n / 9, y = n % 9;
			for(int i = 0; i <= 9; i++) {
				map[x][y] = (char)('0' + i);
				dfs(n + 1);
			}
		}
	}
	public static void main(String[] ar) {
		dfs(0);
	}
}
