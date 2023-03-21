import java.util.Scanner;

/**
 * Dynamic programming
 * */
public class boj1003 {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        int[] N = new int[T];
        //d[i][j] = i번째 피보나치 수을 계산할 때 j가 출력된 횟수
        int[][] d = new int[41][2];
        d[0][0] = 1;
        d[0][1] = 0;
        d[1][0] = 0;
        d[1][1] = 1;

        for (int i = 2; i <= 40; i++) {
            d[i][0] = d[i - 1][0] + d[i - 2][0];
            d[i][1] = d[i - 1][1] + d[i - 2][1];
        }
        for (int i = 0; i < T; i++) {
            N[i] = sc.nextInt();
        }
        for (int i : N) {
            System.out.println(d[i][0] + " " + d[i][1]);
        }

    }
}
