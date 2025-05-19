# https://school.programmers.co.kr/learn/courses/30/lessons/181920

class Solution {
    public int[] solution(int start_num, int end_num) {
        int[] answer = new int[end_num-start_num+1];
        int i=0;
        for(int start=start_num; start<=end_num; start++){
            answer[i]=start;
            i++;
        }
        return answer;
    }
}
