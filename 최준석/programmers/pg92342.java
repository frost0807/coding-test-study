import java.util.Arrays;
/**
 * 백트래킹
 * 고전적인 백트래킹 방식으로 해결했지만,
 * 해당 과녁에 화살을 쏘려고 할 때,
 *
 * 1. 해당 과녁에서 점수를 획득하는 경우
 * 2. 해당 과녁을 포기하는 경우
 * 3. 해당 과녁에 화살을 모두 쏘는 경우
 *
 * 3가지 경우의 수에 대해 DFS를 적용해 해결할 수도 있다.
 */

class Solution {
    int maxScoreGap = 0;
    int[] apeach;
    int[] lion = new int[11];
    int[] result = new int[11];
    int n;

    public int[] solution(int n, int[] info) {
        this.apeach = info;
        this.n = n;
        int[] none = {-1};

        backTrack(0);

        return maxScoreGap != 0 ? result : none;
    }

    public void backTrack(int indexToBeFilled) {
        //화살을 다 쐈으면 계산
        if(n == 0) {
            int apeachScore = 0;
            int lionScore = 0;
            for(int i = 0; i < 11; i++) {
                //둘다 해당 과녁을 맞췄으면 라이언이 더 많이 맞췄을 때만 라이언 승
                if(apeach[i] != 0 && lion[i] != 0) {
                    if(apeach[i] >= lion[i]) {
                        apeachScore += 10-i;
                    } else {
                        lionScore += 10-i;
                    }
                } else if(apeach[i] != 0) {
                    apeachScore += 10-i;
                } else if(lion[i] != 0) {
                    lionScore += 10-i;
                }
            }
            //점수차 비교해서 최대값과 비교
            if(maxScoreGap < lionScore - apeachScore) {
                maxScoreGap = lionScore - apeachScore;
                result = Arrays.copyOf(lion, lion.length);
            } else if(maxScoreGap != 0 && maxScoreGap == lionScore - apeachScore) {
                for(int j = 10; j >= 0; j--) {
                    if(lion[j] > result[j]) {
                        result = Arrays.copyOf(lion, lion.length);
                        break;
                    }
                    if(lion[j] < result[j]) {
                        break;
                    }
                }
            }
            return;
        }

        //아직 다 안 쐈으면 해당 과녁에 화살수가 0개부터 n개 일때까지 다음 index 계산
        for(int i = 0; i <= n; i++) {
            //마지막 과녁인데 화살이 남았다면 다 쏘기
            if(indexToBeFilled == 10) {
                int tempN;
                tempN = n;
                lion[indexToBeFilled] = n;
                n = 0;
                backTrack(indexToBeFilled + 1);
                n =  tempN;
                lion[indexToBeFilled] = 0;
            } else {
                //남은 화살 수 에서 쏜 화살 수 빼주고
                n -= i;
                //해당 과녁에 화살 수 추가
                lion[indexToBeFilled] = i;
                //다음 과녁
                backTrack(indexToBeFilled + 1);
                n += i;
                lion[indexToBeFilled] = 0;
            }
        }
    }
}