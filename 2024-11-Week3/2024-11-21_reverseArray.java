# https://school.programmers.co.kr/learn/courses/30/lessons/120821
class Solution {
    public int[] solution(int[] num_list) {
        int[] answer = new int[num_list.length];
        int z = 0;
        
        for(int n=num_list.length-1; n>=0; n--){
            answer[z] = num_list[n];
            z++;
        }
        
        return answer;
    }
}
