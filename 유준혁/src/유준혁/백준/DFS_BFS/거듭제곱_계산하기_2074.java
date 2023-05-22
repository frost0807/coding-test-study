package 유준혁.백준.DFS_BFS;
import java.util.*;
public class 거듭제곱_계산하기_2074 {
	public static void main (String[] args) {
	    Scanner sc = new Scanner(System.in);
		int n = 20000, step = 1000;
		int[] vst = new int[n + 1];
		Arrays.fill(vst, 1 << 30);
		vst[0] = vst[1] = 0;
		Queue<int[]> q = new LinkedList<>();
		q.add(new int[] { 1, 0, 0 });
		Set<String> set = new HashSet<>();
		set.add("1,0");
		while(!q.isEmpty()) {
		    int[] p = q.poll();
		    int x = p[0], y = p[1], v = p[2] + 1;
		    int[] values = { x * 2, x + y, x - y, y - x, y * 2 };
		    for(int i : values) {
				if (Math.abs(i) > n * 10) continue;
		        if (0 <= i && i <= n && vst[i] >= v) {
		            vst[i] = v;
		        }
				if (v < 19) {
					String xstr = x + "," + i, ystr = i + "," + y;
					if (set.add(xstr)) q.add(new int[] { x, i, v });
					if (set.add(ystr)) q.add(new int[] { i, y, v });
				}
		    }
		}
		System.out.print(Arrays.toString(vst));
	}
}