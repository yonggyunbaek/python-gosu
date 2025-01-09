# https://school.programmers.co.kr/learn/courses/30/lessons/120845

class Solution {
    public int solution(int[] box, int n) {
        int answer = 1;
        for(int b:box){
            if(b/n==0){
                return 0;
            }
            else{
                int cnt = b / n;
                answer *= cnt;
            }
        }
        return answer;
    }
}
