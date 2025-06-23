# https://school.programmers.co.kr/learn/courses/30/lessons/181927
import java.util.Arrays;
class Solution {
    public int[] solution(int[] num_list) {
        int len = num_list.length;
        int[] answer = Arrays.copyOf(num_list, len + 1);
        
        if(answer[len-1]>answer[len-2]){
            answer[len]=answer[len-1]-answer[len-2];
        }
        else{
            answer[len]=answer[len-1]*2;
        }
        
        return answer;
    }
}
