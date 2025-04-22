# https://school.programmers.co.kr/learn/courses/30/lessons/181853

import java.util.Arrays;

class Solution {
    public int[] solution(int[] num_list) {
        int[] answer = new int[5];
        Arrays.sort(num_list);
        int j = 0;
        for(int i=0; i<5; i++){
            answer[j] = num_list[i];
            j++;
        }
        
        return answer;
    }
}
