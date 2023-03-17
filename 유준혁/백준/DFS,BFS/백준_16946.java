// https://www.acmicpc.net/problem/16946
// 예전에 냈다가 틀렸던 풀이
// BFS 2번 반복 > Set에 정점 저장해두고 재사용 하는 방식으로 변경
import java.util.*;
import java.io.*;
class Main {
	static int n, m, cnt;
	static int[][] map, WH = new int [][] {{1, 0, -1, 0}, {0, 1, 0, -1}};
	static void BFS(int i, int j) {
		cnt = 1;
		Queue<int[]> road = new LinkedList<>();
		Set<Integer> wall = new HashSet<>();
		road.add(new int[] {i, j});
		map[i][j] = -1;
		while(!road.isEmpty()) {
			int[] poll = road.poll();
			int a = poll[0], b = poll[1];
			for(int k = 0; k < 4; k++) {
				int A = a + WH[0][k];
				int B = b + WH[1][k];
				if(0 <= A && 0 <= B && A < n && B < m) {
					if (map[A][B] == 0) {
						road.add(new int[] {A, B});
						map[A][B] = -1;
						cnt++;
					} else if (map[A][B] > 0) {
						wall.add(A * 10000 + B);
					}
				}
			}
		}
		wall.forEach(x -> map[x / 10000][x % 10000] += cnt);
	}
	static int Int(String s) {return Integer.parseInt(s);}
	public static void main(String[] ar) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuffer sb = new StringBuffer();
		StringTokenizer st = new StringTokenizer(br.readLine());
		n = Int(st.nextToken()); m = Int(st.nextToken());
		map = new int[n][m];
		for(int i = 0; i < n; i++) {
			String[] input = br.readLine().split("");
			for(int j = 0; j < m; j++) {
				map[i][j] = Int(input[j]);
			}
		}

		for(int i = 0; i < n; i++) {
			for(int j = 0; j < m; j++) {
				if(map[i][j] == 0) BFS(i, j);
			}
		}
		for(int[] arr : map) {
			for(int i : arr) {
				sb.append(i == -1 ? 0 : (i % 10));
			}
			sb.append("\n");
		}
		System.out.print(sb.toString());
	}
}