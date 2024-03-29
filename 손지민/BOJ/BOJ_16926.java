package 손지민.BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ_16926 {
    private static BufferedReader br;
    private static StringTokenizer st;
    private static int N;
    private static int M;
    private static int R;
    private static int[][] A;
    private static int group = 0;
    private static int[] dy = {0, 1, 0, -1}; // 오 -> 왼, 아래 -> 위, 왼 -> 오, 위 -> 아래
    private static int[] dx = {1, 0, -1, 0};


    public static void print() {
        for (int i = 0; i < A.length; i++) {
            for (int j = 0; j < A[i].length; j++) {
                System.out.print(A[i][j] + " ");
            }
            System.out.println();
        }
    }

    public static boolean isRange(int y, int x, int i) {
        return i <= y && y < N - i && i <= x && x < M - i;
    }

    public static void rotate() {
        for (int i = 0; i < group; i++) {
            int y = i, x = i;
            int first = A[y][x];

            int idx = 0;
            while (idx < 4) {
                int ny = y + dy[idx];
                int nx = x + dx[idx];

                if(isRange(ny, nx, i)) {
                    A[y][x] = A[ny][nx];
                    y = ny;
                    x = nx;
                }
                else idx += 1;
            }
            A[i + 1][i] = first;
        }
    }

    public static void main(String[] args) throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        R = Integer.parseInt(st.nextToken());

        A = new int[N][M];
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < M; j++) {
                A[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        group = Math.min(N, M) / 2;
        while (R-- > 0) rotate();
        print();
    }
}
