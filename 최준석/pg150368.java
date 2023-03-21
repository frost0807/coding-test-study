/**
*백트래킹 문제
*/
class Solution {
    //result[0]은 조건을 만족하는 최대 가입자수
    //result[1]은 조건을 만족하는 최대 이모티콘 판매비용
    int[] result = {0, 0};
    int emoticonCount;
    int[] emoticons;
    int[] discountRatePerEmoticon;
    int[] discountRates = {0, 10, 20, 30, 40};
    int[][] users;
    
    public int[] solution(int[][] users, int[] emoticons) {
        emoticonCount = emoticons.length;
        this.emoticons = emoticons;
        this.users = users;
        this.discountRatePerEmoticon = new int[emoticonCount];
        
        backTrack(0);
        
        return result;
    }
    
    //index번째 이모티콘의 할인율 책정
    public void backTrack(int indexToBeFilled) {
        if(indexToBeFilled == emoticonCount) {
            int[] tempResult = {0, 0};
            
            for(int[] user : users) {
                int usedPrice = 0;
                for(int i = 0; i < emoticonCount; i++) {
                    if(discountRatePerEmoticon[i] >= user[0]) {
                        usedPrice += emoticons[i] - 
                            (emoticons[i] * discountRatePerEmoticon[i] /100);
                    }
                }
                if(usedPrice >= user[1]) {
                    tempResult[0]++;
                    usedPrice = 0;
                }
                tempResult[1] += usedPrice;
            }
            if(result[0] < tempResult[0]) {
                result[0] = tempResult[0];
                result[1] = tempResult[1];
            } else if(result[0] == tempResult[0] && result[1] < tempResult[1]) {
                result[0] = tempResult[0];
                result[1] = tempResult[1];
            }
            return;
        }
        
        for(int i = 0; i < 5; i++) {
            discountRatePerEmoticon[indexToBeFilled] = discountRates[i];
            backTrack(indexToBeFilled + 1);
        }
    }
}