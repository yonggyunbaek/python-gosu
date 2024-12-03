# https://school.programmers.co.kr/learn/courses/30/lessons/120910
class Solution {
    public int solution(int n, int t) {
        int answer = n;
        for(int i=1; i<=t; i++){
            answer *= 2;
        }
        return answer;
    }
}
