# https://school.programmers.co.kr/learn/courses/30/lessons/181852

import java.util.Arrays;

class Solution {
    public int[] solution(int[] num_list) {
        int[] answer = new int[num_list.length-5];
        Arrays.sort(num_list);
        int j = 0;
        for(int i=5;i<num_list.length;i++){
            answer[j] = num_list[i];
            j++;
        }
        return answer;
    }
}
