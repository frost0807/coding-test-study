import java.util.*;
class Main {
	public static void main (String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt(), m = sc.nextInt(), INF = 1 << 25;
		int[] dist = new int[n + 1], route = new int[n + 1];
		Arrays.fill(dist, INF);
		int[][] bus = new int[n + 1][n + 1];
		for(int i = 0; i <= n; i++) Arrays.fill(bus[i], INF);
		for(int i = 0; i < m; i++) {
			int s = sc.nextInt(), e = sc.nextInt(), t = sc.nextInt();
			bus[s][e] = Math.min(bus[s][e], t);
		}
		int s = sc.nextInt(), e = sc.nextInt();
		PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> a[1] - b[1]);
		dist[s] = 0;
		pq.add(new int[] {s, 0, s});
		while(!pq.isEmpty()) {
			int[] p = pq.poll();
			int a = p[0], d = p[1], r = p[2];
			if (d > dist[a]) continue;
			route[a] = r;
			for(int i = 0; i <= n; i++) {
				int next = bus[a][i] + d;
				if (next < dist[i]) {
					pq.add(new int[] {i, next, a});
					dist[i] = next;
				}
			}
		}
		System.out.println(dist[e]);
		List<Integer> list = new ArrayList<>();
		list.add(e);
		while(e != route[e]) list.add(e = route[e]);
		list.sort((a, b) -> -1);
		System.out.println(list.size());
		for(int i : list) System.out.print(sb + " ");
	}
}