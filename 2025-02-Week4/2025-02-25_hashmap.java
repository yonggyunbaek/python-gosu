# https://school.programmers.co.kr/learn/courses/30/lessons/120894

import java.util.HashMap;
import java.util.Map;

class Solution {
    public long solution(String numbers) {
        StringBuilder sb = new StringBuilder();
        Map<String, String> numberMap = new HashMap<>();
        
        numberMap.put("zero", "0");
        numberMap.put("one", "1");
        numberMap.put("two", "2");
        numberMap.put("three", "3");
        numberMap.put("four", "4");
        numberMap.put("five", "5");
        numberMap.put("six", "6");
        numberMap.put("seven", "7");
        numberMap.put("eight", "8");
        numberMap.put("nine", "9");
        
        int start = 0;
        for(int end=0; end <= numbers.length(); end++){
            String num = numbers.substring(start,end);
            if(numberMap.containsKey(num)){
                sb.append(numberMap.get(num));
                start = end;
            }
        }
        // System.out.println(sb);
        long answer = Long.valueOf(sb.toString());
        return answer;
    }
}
