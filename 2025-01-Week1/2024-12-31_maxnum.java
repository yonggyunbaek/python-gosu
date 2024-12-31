# https://school.programmers.co.kr/learn/courses/30/lessons/120899

class Solution {
    public int[] solution(int[] array) {
        int[] answer = {0, 0};
        int max_num = array[0];
        int index = 0;
        
        for(int i=0; i < array.length; i++){
            if(array[i] > max_num){
                max_num = array[i];
                index = i;
            }
        }
        answer[0] = max_num;
        answer[1] = index;
        
        return answer;
    }
}
