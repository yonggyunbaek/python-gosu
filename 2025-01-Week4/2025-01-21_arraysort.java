# https://school.programmers.co.kr/learn/courses/30/lessons/120850

import java.util.ArrayList;
import java.util.Collections;

class Solution {
    public int[] solution(String my_string) {
        ArrayList<Integer> array = new ArrayList<>(); 
        char cur_char;
        
        for(int i=0; i<my_string.length();i++){
            cur_char = my_string.charAt(i);
            if(cur_char >= '0' && cur_char <= '9'){
                array.add(cur_char - '0');
            }
        }
        Collections.sort(array);
        int[] answer = new int[array.size()];
        for (int i = 0; i < array.size(); i++) {
            answer[i] = array.get(i);
        }
        return answer;
    }
}
