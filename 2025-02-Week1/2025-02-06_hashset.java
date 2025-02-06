# https://school.programmers.co.kr/learn/courses/30/lessons/120888

import java.util.Set;
import java.util.HashSet;

class Solution {
    public String solution(String my_string) {
        if (my_string == null || my_string.isBlank()) {
            return my_string;
        }

        StringBuilder sb = new StringBuilder();
        Set<Character> set = new HashSet<>();
        
        for (char c : my_string.toCharArray()) {
            if (set.add(c)) {
                sb.append(c);
            }
        }
        return sb.toString();
    }
}
