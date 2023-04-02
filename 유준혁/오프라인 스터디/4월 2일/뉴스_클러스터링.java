import java.util.*;
class Solution {
    public int solution(String str1, String str2) {
        int answer = 0;
        // 대문자로 통일
        str1 = str1.toUpperCase();
        str2 = str2.toUpperCase();
        
        // n-gram을 체크하기 위한 해시맵
        Map<String, Integer> map1 = new HashMap<>(), map2 = new HashMap<>();
        char[] arr1 = str1.toCharArray(), arr2 = str2.toCharArray();
        // 복붙 대신 포문으로 돌림
        for(int j = 0; j < 2; j++) {
            char[] arr = j == 0 ? arr1 : arr2;
            Map<String, Integer> map = j == 0 ? map1 : map2;
            // n-gram (n = 2) 확인
            for(int i = 0; i < arr.length - 1; i++) {
                String tmp = arr[i] + "" + arr[i+1];
                // 문자로만 이루어졌는지 확인
                if(tmp.matches("[a-zA-Z]{2}") == false) continue;
                int val = map.getOrDefault(tmp, 0);
                map.put(tmp, val + 1);
            }
        }
        // a = 교집합
        double a = 0, b = 0;
        for(String key : map1.keySet()) {
            a += map2.containsKey(key) ? Math.min(map1.get(key), map2.get(key)) : 0;
            map2.put(key, Math.max(map1.get(key), map2.getOrDefault(key, 0)));
        }
        // b = 합집합
        for(int val : map2.values()) b += val;
        return a == 0 && b == 0 ? 65536 : (int)((a / b) * 65536);
    }
}