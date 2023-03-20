import java.util.LinkedList;
import java.util.Queue;

class Solution {
    public int solution(int cacheSize, String[] cities) {
        Queue<String> cache = new LinkedList<>();
        int totalTime = 0;
        
        for(String city : cities) {
            if(cacheSize == 0) {
                return cities.length * 5;
            }
            city = city.toLowerCase();
            
            //cache hit이면 시간 1 추가하고 cache 재정렬
            if(cache.remove(city)) {
                totalTime += 1;
                cache.add(city);
            } else {
                //cache miss이면 시간 5 추가하고 cache 용량 확인 후 캐시추가 or 캐시 갱신
                totalTime += 5;
                if(cache.size() < cacheSize) {
                    cache.add(city);
                } else {
                    cache.poll();
                    cache.add(city);
                }
            }
        }
        return totalTime;
    }
}