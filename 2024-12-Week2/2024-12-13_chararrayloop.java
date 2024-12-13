# https://school.programmers.co.kr/learn/courses/30/lessons/120849

import java.util.Arrays;

class Solution {
    public String solution(String my_string) {
        String answer = "";
        Character[] aeiou = new Character[]{'a', 'e', 'i', 'o', 'u'};
        
        for(int i=0; i<my_string.length();i++){
            if(Arrays.asList(aeiou).contains(my_string.charAt(i))){
                continue;
            }
            else{
                answer += my_string.charAt(i);
            }
        }
        
        return answer;
    }
}
