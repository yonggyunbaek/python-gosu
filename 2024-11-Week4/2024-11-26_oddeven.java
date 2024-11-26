# https://school.programmers.co.kr/learn/courses/30/lessons/120824

class Solution {
    public int[] solution(int[] num_list) {
        int even = 0;
        int odd = 0;
        
        int[] answer = new int[2];
        
        for(int num:num_list){
            if(num%2==0){
                even++;
            }
            else{
                odd++;
            }
        }
        
        answer[0]=even;
        answer[1]=odd;
        
        return answer;
    }
}
