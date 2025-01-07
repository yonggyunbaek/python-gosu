# https://school.programmers.co.kr/learn/courses/30/lessons/120834

class Solution {
    public String solution(int age) {
        String answer = "";
        String String_age = String.valueOf(age);
        for (int index = 0; index < String_age.length(); index++) {
            char ans = (char)((String_age.charAt(index) - '0') + 'a');
            answer += ans;
        }
        return answer;
    }
}
