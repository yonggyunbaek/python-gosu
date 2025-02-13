# https://school.programmers.co.kr/learn/courses/30/lessons/120896#
import java.util.*;

class Solution {
    public String solution(String s) {
        Map<Character, Integer> map = new HashMap<>();
        StringBuilder sb = new StringBuilder();

        for (char c : s.toCharArray()) {
            map.put(c, map.getOrDefault(c, 0) + 1);
        }

        List<Character> uniqueChars = new ArrayList<>();
        for (Map.Entry<Character, Integer> entry : map.entrySet()) {
            if (entry.getValue() == 1) {
                uniqueChars.add(entry.getKey());
            }
        }
        Collections.sort(uniqueChars);
        for (char c : uniqueChars) {
            sb.append(c);
        }
        return sb.toString();
    }
}
