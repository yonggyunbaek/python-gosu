# https://school.programmers.co.kr/learn/courses/30/lessons/120819
class Solution {
    public int[] solution(int money) {
        int[] answer = {0,0};
        
        while(money >= 5500){
            money -= 5500;
            answer[0] = answer[0] + 1;
        }
        answer[1] = money;
        return answer;
}
    }
