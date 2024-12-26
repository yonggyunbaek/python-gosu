# https://school.programmers.co.kr/learn/courses/30/lessons/120851

class Solution {
    public int solution(String my_string) {
        int answer = 0;
        for(int i=0; i<my_string.length(); i++){
            if(Character.isDigit(my_string.charAt(i))){
                // System.out.println(my_string.charAt(i));
                int num = my_string.charAt(i) - '0';
                answer = answer + num;
                // System.out.println(answer);
            }            
        }
        
        return answer;
    }
}
