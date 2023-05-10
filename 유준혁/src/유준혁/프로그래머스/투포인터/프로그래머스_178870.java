import java.util.*;
class Solution {
    public int[] solution(int[] seq, int k) {
        List<int[]> list = new ArrayList<>();
        int sum = 0, l = 0, r = 0, n = seq.length;
        while(l <= r && r < n) {
            sum += seq[r];
            if (sum >= k) {
                while(sum > k) {
                    sum -= seq[l];
                    l++;
                }
                if (sum == k) list.add(new int[] { l, r });
            }
            r++;
        }
        list.sort((a, b) -> {
            int adis = a[1] - a[0];
            int bdis = b[1] - b[0];
            return adis == bdis ? a[0] - b[0] : (adis - bdis);
        });
        return list.get(0);
    }
}