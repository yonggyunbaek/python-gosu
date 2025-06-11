# https://school.programmers.co.kr/learn/courses/30/lessons/181909
import java.util.Arrays;

class Solution {
    public String[] solution(String my_string) {
        String[] answer = new String[my_string.length()];
        int len = my_string.length();
        for(int i=0 ; i<len;i++){
            answer[i] = my_string.substring(len-i-1,len);
        }
        Arrays.sort(answer);
        return answer;
    }
}
