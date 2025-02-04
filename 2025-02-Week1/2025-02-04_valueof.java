# https://school.programmers.co.kr/learn/courses/30/lessons/120891

class Solution {
    public int solution(int order) {
        String order_string = String.valueOf(order);
        
        int answer = 0;
        for(int i=0; i<order_string.length();i++){
            int num = Character.getNumericValue(order_string.charAt(i));
            if (num != 0 && num % 3 == 0){
                answer++;
            }
        }
        return answer;
    }
}
