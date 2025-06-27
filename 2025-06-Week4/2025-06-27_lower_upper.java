# https://school.programmers.co.kr/learn/courses/30/lessons/181874

class Solution {
    public String solution(String myString) {
        String answer = "";
        String[] tmp = myString.split("");
        for(String t:tmp){
            if(t.equals("a") | t.equals("A")){
                answer += t.toUpperCase();
            }
            else{
                answer += t.toLowerCase();
            }
            
        }
        return answer;
    }
}
