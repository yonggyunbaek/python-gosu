# https://school.programmers.co.kr/learn/courses/30/lessons/120830

class Solution {
    public int solution(int n, int k) {
        int remain = n/10;
        k = k - remain;
            
        return n * 12000 + k * 2000;
    }
}
