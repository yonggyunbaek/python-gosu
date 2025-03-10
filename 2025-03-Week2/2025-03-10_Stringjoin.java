# https://school.programmers.co.kr/learn/courses/30/lessons/120869

import java.util.Arrays;

class Solution {
    public int solution(String[] spell, String[] dic) {
        Arrays.sort(spell);
        String answer = String.join("", spell);
        // System.out.println(answer);
        for(String d: dic){
            char[] charArray = d.toCharArray();
            Arrays.sort(charArray);
    
            String ans = new String(charArray);
            
            // System.out.println(ans);
            if(answer.equals(ans)){
                return 1;
            }
        }
        return 2;
    }
}
