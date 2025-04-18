# https://school.programmers.co.kr/learn/courses/30/lessons/181892

class Solution {
    public int[] solution(int[] num_list, int n) {
        int[] answer = new int[num_list.length - (n - 1)];
        for (int i = n - 1; i < num_list.length; i++) {
            answer[i - (n - 1)] = num_list[i];
        }
        return answer;
    }
}
