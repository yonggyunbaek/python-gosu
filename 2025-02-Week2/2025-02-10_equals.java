# https://school.programmers.co.kr/learn/courses/30/lessons/120886

import java.util.Arrays;

class Solution {
    public int solution(String before, String after) {
        char[] before_charArray = before.toCharArray();
        char[] after_charArray = after.toCharArray();
        
        Arrays.sort(before_charArray);
        Arrays.sort(after_charArray);
        
        String b_str = new String(before_charArray);
        String a_str = new String(after_charArray);
        
        if(b_str.equals(a_str)){
            return 1;
        }
        else{
            return 0;
        }
    }
}
