# https://school.programmers.co.kr/learn/courses/30/lessons/120839

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

class Solution {
    public String solution(String rsp) {
        Map<String, String> hashMap = new HashMap<>();
        String answer = "";
        
        hashMap.put("2", "0");
        hashMap.put("0", "5");
        hashMap.put("5", "2");
        
        for(int i=0; i<rsp.length(); i++){
            String key = hashMap.get(String.valueOf(rsp.charAt(i)));
            answer += key;            
        }
        
        return answer;
    }
}
