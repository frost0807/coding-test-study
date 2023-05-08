import java.util.*;
class Solution {
    public int[] solution(int target) {
        int INF = 987654321, limit = 2000001;
        int[][] dist = new int[limit][2];
        for(int i = 1; i < limit; i++) Arrays.fill(dist[i], INF);
        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> {
            if (a[0] == b[0]) return b[1] - a[1];
            return a[0] - b[0];
        });
        pq.add(new int[] { 0, 0, 0 });
        while(!pq.isEmpty()) {
            int[] p = pq.poll();
            int t = p[0], c = p[1], sb = p[2];
            for(int i = 1; i <= 3; i++) {
                for(int j = 1; j <= 20; j++) {
                    int nt = t + i * j;
                    int nc = c + 1;
                    int nsb = sb + (i == 1 ? 1 : 0);
                    if (nt > target) continue;
                    if (dist[nt][0] > nc || (dist[nt][0] == nc && dist[nt][1] < nsb)) {
                        dist[nt][0] = nc;
                        dist[nt][1] = nsb;
                        pq.add(new int[] { nt, nc, nsb });
                    }
                }
            }
            if (t + 50 > target) continue;
            int nt = t + 50;
            int nc = c + 1;
            int nsb = sb + 1;
            if (dist[nt][0] > nc || (dist[nt][0] == nc && dist[nt][1] < nsb)) {
                dist[nt][0] = nc;
                dist[nt][1] = nsb;
                pq.add(new int[] { nt, nc, nsb });
            }
        }
        return dist[target];
    }
}