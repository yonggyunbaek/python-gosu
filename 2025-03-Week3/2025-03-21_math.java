# https://school.programmers.co.kr/learn/courses/30/lessons/120924

class Solution {
    public int solution(int[] common) {
        int n = common.length;

        if (2 * common[1] == common[0] + common[2]) {
            int diff = common[1] - common[0];
            return common[n - 1] + diff;
        }

        else if (common[1] * common[1] == common[0] * common[2]) {
            int ratio = common[1] / common[0];
            return common[n - 1] * ratio;
        }
        
        return 0;
    }
}
