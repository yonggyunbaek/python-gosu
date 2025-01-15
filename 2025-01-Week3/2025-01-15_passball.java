# https://school.programmers.co.kr/learn/courses/30/lessons/120843

class Solution {
    public int solution(int[] numbers, int k) {
        int index = 0;
        for(int i=1; i<k; i++){
            index += 2;
        }
        if(index<numbers.length){
            return numbers[index];
        }
        else{
            index %= numbers.length;
            return numbers[index];
        }
        
    }
}
