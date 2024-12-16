# https://school.programmers.co.kr/learn/courses/30/lessons/120847

import java.util.Arrays;

class Solution {
    public int solution(int[] numbers) {
        Arrays.sort(numbers);
        int n = numbers.length;
        return numbers[n - 1] * numbers[n - 2];
    }
}
