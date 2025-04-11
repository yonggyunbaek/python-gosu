# https://school.programmers.co.kr/learn/courses/30/lessons/181928

class Solution {
    public int solution(int[] num_list) {
        String odd = "";
        String even = "";
        
        for(int num:num_list){
            if(num%2==1){
                odd += num;
            }
            else{
                even += num;
            }
        }
        Integer answer = Integer.valueOf(odd) + Integer.valueOf(even);
        return answer;
    }
}
