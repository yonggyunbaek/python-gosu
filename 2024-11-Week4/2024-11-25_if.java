# https://school.programmers.co.kr/learn/courses/30/lessons/120841
class Solution {
    public int solution(int[] dot) {
        int answer = 0;
        
        if(dot[0] > 0 && dot[1] > 0){
            answer = 1;  
        }
        else if(dot[0] > 0 && dot[1] < 0){
            answer = 4;
        }
        else if(dot[0] < 0 && dot[1] > 0){
            answer = 2;
        }
        else{
            answer = 3;
        }
        return answer;
    }
}