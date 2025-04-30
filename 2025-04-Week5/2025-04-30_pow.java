# https://school.programmers.co.kr/learn/courses/30/lessons/181929

class Solution {
    public int solution(int[] num_list) {
        int num1 = 1;
        int num2 = 0;
        for(int num:num_list){
            num1*=num;
            num2+=num;
        }
        num2 = (int)Math.pow(num2, 2);
        if(num1>num2){
            return 0;
        }
        else{
            return 1;
        }
    }
}
