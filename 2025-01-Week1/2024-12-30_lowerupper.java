# https://school.programmers.co.kr/learn/courses/30/lessons/120893

class Solution {
    public String solution(String my_string) {
        String answer = "";
        for(int i=0; i<my_string.length(); i++){
            char x = my_string.charAt(i);
            char y = 0;
            if(Character.isLowerCase(x)){
                y = Character.toUpperCase(x);
            }
            else if(Character.isUpperCase(x)){
                y = Character.toLowerCase(x);
            }
            answer = answer + y;
        }
        return answer;
    }
}

# 조건문 안에서 선언하면 그 밖에서는 사용안됨.
