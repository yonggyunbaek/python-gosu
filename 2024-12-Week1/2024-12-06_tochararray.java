# https://school.programmers.co.kr/learn/courses/30/lessons/120826

class Solution {
    public String solution(String my_string, String letter) {
        String answer = "";
        char[] arr = my_string.toCharArray();
        for(char a: arr){
            if(a!=letter.charAt(0)){
                answer += a;
            }
        }
        
         return answer;
    }
}
