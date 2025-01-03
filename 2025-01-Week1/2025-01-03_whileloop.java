# https://school.programmers.co.kr/learn/courses/30/lessons/120815
class Solution {
    public int solution(int n) {
        int cnt = 1;
        while(true){
            if((cnt*6) % n == 0){
                return cnt;
            }
            else{
                cnt++;
            }
        }
    }
}
