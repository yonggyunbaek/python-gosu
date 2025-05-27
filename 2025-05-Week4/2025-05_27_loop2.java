# https://school.programmers.co.kr/learn/courses/30/lessons/181891

class Solution {
    public int[] solution(int[] num_list, int n) {
        int[] answer = new int[num_list.length];
        for(int i=0;i<num_list.length;i++){
            if(n>=num_list.length){
                answer[i]=num_list[n-num_list.length];
            }
            else{
                answer[i]=num_list[n];            
            }
            n++;
        }
        
        return answer;
    }
}
