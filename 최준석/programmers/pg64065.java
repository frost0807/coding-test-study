import java.util.Arrays;
import java.util.Comparator;
import java.util.LinkedHashSet;

class Solution {
    public int[] solution(String s) {
        int[] result;
        //맨 앞의 {{와 맨 뒤의 }} 제거
        s = s.substring(1, s.length() - 1);
        //원소가 1개이면,
        if(!s.contains("},{")) {
            //해당 원소를 Integer로 변환
            int element = Integer.parseInt(s.substring(1, s.length() - 1));
            result = new int[1];
            result[0] = element;

            return result;
            //원소가 2개 이상이라면,
        } else {
            //각 원소들을 분리하기 위해 ,로 split
            String[] elements = s.substring(1, s.length() - 1).split("[{]");
            result = new int[elements.length];
            LinkedHashSet<Integer> set = new LinkedHashSet<>();
            //원소의 인자갯수를 기준으로 정렬
            Arrays.sort(elements, new TupleComparator());
            for(int i = 0; i < elements.length; i++) {
                elements[i] = elements[i].replace("},", "");
                for(String element:elements[i].split(",")) {
                    set.add(Integer.parseInt(element));
                }
            }
            result = set.stream().mapToInt(Integer::intValue).toArray();
            return result;
        }
    }
}

class TupleComparator implements Comparator<String> {
    public int compare(String e1, String e2) {
        return e1.split(",").length - e2.split(",").length;
    }
}