// https://school.programmers.co.kr/learn/courses/30/lessons/142085?language=java
// JS에 우선순위 큐 기본 라이브러리가 없어 자바로 품
// 앞에서부터 라운드 진행하며 막혔을 경우 가장 많은 적을 상대한 라운드를 무효처리
import java.util.*;
class Solution {
    public int solution(int n, int k, int[] enemy) {
        int i = 0;
        PriorityQueue<Integer> pq = new PriorityQueue<>((a, b) -> b - a);
        for(; i < enemy.length; i++) {
            int e = enemy[i];
            pq.add(e);
            n -= e;
            if(n < 0) {
                if (k > 0) {
                    int p = pq.poll();
                    n += p;
                    k--;
                } else break;
            }
        }
        return i;
    }
}