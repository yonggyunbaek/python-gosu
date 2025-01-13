# https://school.programmers.co.kr/learn/courses/30/lessons/120840

class Solution {
    public int solution(int balls, int share) {
        long result = 1;

        for (int i = 0; i < share; i++) {
            result *= (balls - i);
            result /= (i + 1);
        }

        return (int)result;
    }
}
