# https://school.programmers.co.kr/learn/courses/30/lessons/120811

import java.util.Arrays;
class Solution {
    public int solution(int[] array) {
        int n = array.length / 2;
        
        Arrays.sort(array);
        int answer = array[n];
        return answer;
    }
}
