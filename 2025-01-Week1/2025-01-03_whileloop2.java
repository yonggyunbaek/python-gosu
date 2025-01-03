# https://school.programmers.co.kr/learn/courses/30/lessons/120816
class Solution {
    public int solution(int slice, int n) {
        int cnt = 1;
        while(slice * cnt < n){
            cnt++;
        }
        return cnt;
    }
}
