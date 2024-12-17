# https://school.programmers.co.kr/learn/courses/30/lessons/120814

class Solution {
    public int solution(int n) {
        int answer = 0;
        if(n%7==0){
            return n/7;
        }
        else{
            return n/7 + 1;
        }
    }
}
