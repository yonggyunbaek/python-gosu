# https://school.programmers.co.kr/learn/courses/30/lessons/120890

class Solution {
    public int solution(int[] array, int n) {
        int answer = 0;
        int cur_num = Integer.MAX_VALUE;
        
        for (int num : array) {
            int diff = Math.abs(num - n);
            if (diff < cur_num || (diff == cur_num && num < answer)) {
                answer = num;
                cur_num = diff;
            }
        }
        
        return answer;
    }
}
