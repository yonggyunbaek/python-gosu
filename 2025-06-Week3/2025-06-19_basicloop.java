#https://school.programmers.co.kr/learn/courses/30/lessons/181896

class Solution {
    public int solution(int[] num_list) {
        int answer = -1;
        for(int i=0;i<num_list.length;i++){
            if(num_list[i]<0){
                return i;
            }
        }
        
        return answer;
    }
}
