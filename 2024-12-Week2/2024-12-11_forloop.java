# https://school.programmers.co.kr/learn/courses/30/lessons/120585

class Solution {
    public int solution(int[] array, int height) {
        int answer = 0;
        for(int a:array){
            if(a > height){
                answer++;
            }
        }
        
        return answer;
    }
}
