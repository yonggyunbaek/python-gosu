# https://school.programmers.co.kr/learn/courses/30/lessons/181840

class Solution {
    public int solution(int[] num_list, int n) {
        int answer = 0;
        for(int num:num_list){
            if(num==n){
                return 1;
            }
        }
        return 0;
    }
}
