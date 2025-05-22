# https://school.programmers.co.kr/learn/courses/30/lessons/181884

class Solution {
    public int solution(int[] numbers, int n) {
        int answer = 0;
        for(int i=0; i<numbers.length;i++){
            answer+=numbers[i];
            if(answer>n){
                return answer;
            }
        }
        return answer;
    }
}
