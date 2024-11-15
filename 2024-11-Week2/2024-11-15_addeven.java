# https://school.programmers.co.kr/learn/courses/30/lessons/120831

class Solution {
    public int solution(int n) {
        int answer = 0;

        if (n % 2 != 0) {
            n--;
        }

        for (int i = 2; i <= n; i += 2) {
            answer += i;
        }

        return answer;
    }
}
