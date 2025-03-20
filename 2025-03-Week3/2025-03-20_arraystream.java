# https://school.programmers.co.kr/learn/courses/30/lessons/120880

import java.util.*;

class Solution {
    public int[] solution(int[] numlist, int n) {
        Integer[] arr = Arrays.stream(numlist).boxed().toArray(Integer[]::new);

        Arrays.sort(arr, (a, b) -> {
            int diffA = Math.abs(a - n);
            int diffB = Math.abs(b - n);
            
            if (diffA == diffB) {
                return b - a;
            }
            return diffA - diffB; 
        });

        return Arrays.stream(arr).mapToInt(Integer::intValue).toArray();
    }
}
