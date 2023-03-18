// https://www.acmicpc.net/problem/16139
import java.util.*;
import java.io.*;
class Main {
	static int Int(String s) { return Integer.parseInt(s); }
	public static void main (String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		char[] arr = br.readLine().toCharArray();
		int tc = Int(br.readLine()), n = arr.length;
		int[][] sum = new int[26][n + 1];
		for(int i = 0; i < 26; i++) {
			for(int j = 0; j < n; j++) sum[i][j + 1] = sum[i][j] + (arr[j] == 'a' + i ? 1 : 0);
		}
		StringBuilder sb = new StringBuilder();
		while(tc-->0) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			char a = st.nextToken().charAt(0);
			int s = Int(st.nextToken()), e = Int(st.nextToken()) + 1;
			sb.append(sum[a - 'a'][e] - sum[a - 'a'][s]).append("\n");
		}
		System.out.print(sb);
	}
}