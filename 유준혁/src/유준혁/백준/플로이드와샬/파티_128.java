package 유준혁.백준.플로이드와샬;

import java.util.*;
public class 파티_128 {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt(), m = sc.nextInt(), x = sc.nextInt();
        int[][] arr = new int[n + 1][n + 1];
        for (int[] i: arr) Arrays.fill(i, 987654321);
        for (int i = 0; i < m; i++) {
            arr[sc.nextInt()][sc.nextInt()] = sc.nextInt();
        }
        for (int i = 1; i <= n; i++){
            for (int j = 1; j <= n; j++){
                for (int k = 1; k <= n; k++){
                    if (arr[j][i] + arr[i][k] < arr[j][k]){
                        arr[j][k] = arr[j][i] + arr[i][k];
                    }
                }
            }
        }

        int max = 0;
        for (int i = 1; i <= n; i++){
            if (i == x) continue;
            max = Math.max(max, arr[i][x] + arr[x][i]);
        }
        System.out.println(max);
    }
}
