# https://school.programmers.co.kr/learn/courses/30/lessons/120868

class Solution {
    public int solution(int[] sides) {
        int a = Math.min(sides[0], sides[1]);
        int b = Math.max(sides[0], sides[1]);

        int min_x = Math.abs(a - b) + 1;
        int max_x = a + b - 1;           

        return max_x - min_x + 1;
    }
}
