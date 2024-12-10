# https://school.programmers.co.kr/learn/courses/30/lessons/120903

import java.util.Arrays;
class Solution {
    public int solution(String[] s1, String[] s2) {
        int answer = 0;
        for(String s:s1){
            if(Arrays.asList(s2).contains(s)){
                answer++;
            }
        }
        return answer;
    }
}
