# https://school.programmers.co.kr/learn/courses/30/lessons/120837

class Solution {
    public int solution(int hp) {
        int answer = 0;
        int[] ants = {5, 3, 1};
        
        for(int ant: ants){
            while(hp >= ant){
                hp -= ant;
                answer ++;
                // System.out.println(ant);
            }
        }
        return answer;
    }
}
