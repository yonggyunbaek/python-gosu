#  https://school.programmers.co.kr/learn/courses/30/lessons/120817
class Solution {
    public double solution(int[] numbers) {
        double sum = 0;
        
        for(int num:numbers){
            sum = sum + num;
        }
        
        double answer = sum / numbers.length;
        
        return answer;
    }
}
