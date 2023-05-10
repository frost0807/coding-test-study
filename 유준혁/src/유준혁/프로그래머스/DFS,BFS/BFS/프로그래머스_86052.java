import java.util.*;
class Solution {
    List<Integer> list = new ArrayList<>();
    int n, m;
    boolean[][][] vst;
    char[][] map;
    int[][] wh = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
    public int[] solution(String[] grid) {
        n = grid.length;
        m = grid[0].length();
        map = new char[n][];
        vst = new boolean[n][m][4];
        for(int i = 0; i < n; i++) map[i] = grid[i].toCharArray();
        for(int i = 0; i < n; i++) {
            for(int j = 0; j < m; j++) {
                for(int k = 0; k < 4; k++) {
                    int a = i, b = j, c = k, d = 0;
                    while(!vst[a][b][c]) {
                        vst[a][b][c] = true;
                        a = (a + n + wh[c][0]) % n;
                        b = (b + m + wh[c][1]) % m;
                        c = (c + 4 + (map[a][b] == 'R' ? 1 : map[a][b] == 'L' ? -1 : 0)) % 4;
                        d++;
                        if(vst[a][b][c]) list.add(d);
                    }
                }
            }
        }
        list.sort(null);
        int[] answer = new int[list.size()];
        for(int i = 0; i < answer.length; i++) answer[i] = list.get(i);
        return answer;
    }
}
