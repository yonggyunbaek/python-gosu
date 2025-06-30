# https://school.programmers.co.kr/learn/courses/30/lessons/181873

class Solution {
    public String solution(String my_string, String alp) {
        String answer = "";
        String[] tmp = my_string.split("");
        for(String word:tmp){
            if(word.equals(alp)){
                answer += word.toUpperCase();
            }
            else{
                answer += word;
            }
        }
        return answer;
    }
}
