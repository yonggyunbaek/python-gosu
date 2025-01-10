# https://school.programmers.co.kr/learn/courses/30/lessons/120838?language=java

import java.util.*;

class Solution {
    public String solution(String letter) {
        Map<String,Character> morse_map = new HashMap<>();
        String[] morse = {".-","-...","-.-.","-..",".","..-.","--.",
                          "....","..",".---","-.-",".-..","--","-.",
                          "---",".--.","--.-",".-.","...","-","..-",
                          "...-",".--","-..-","-.--","--.."};
        char alpha = 96;
        for(String m:morse){
            alpha++;
            morse_map.put(m,alpha);
        }
        String answer = "";
        String[] letter_split = letter.split(" ");
        
        for(String l:letter_split){
            // System.out.println(l);
            answer += morse_map.get(l);
        }
        
        return answer;
    }
}
