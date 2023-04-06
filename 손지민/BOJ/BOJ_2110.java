package 손지민.BOJ;

import java.util.Arrays;
import java.util.Scanner;

public class BOJ_2110 {
    public static int N;
    public static int M;
    public static int[] arr;

    public static int solve() {
        int lo = 1;
        int hi = arr[N - 1] - arr[0] + 1;
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if(countRouter(mid) < M){
                hi = mid;
            }else{
                lo = mid + 1;
            }
        }
        return lo-1;
    }

    private static int countRouter(int distance) {
        int cnt = 1;
        int lastLocate = arr[0];

        for (int i = 1; i < arr.length; i++) {
            int currLocate = arr[i];

            if (currLocate - lastLocate >= distance) {
                cnt++;
                lastLocate = currLocate;
            }
        }
        return cnt;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        M = sc.nextInt();

        arr = new int[N];

        for(int i = 0; i < N; i++) {
            arr[i] = sc.nextInt();
        }

        Arrays.sort(arr);
        System.out.println(solve());
    }
}