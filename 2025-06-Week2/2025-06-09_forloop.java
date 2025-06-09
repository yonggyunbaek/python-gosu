# https://school.programmers.co.kr/learn/courses/30/lessons/181888

class Solution {
    public int[] solution(int[] num_list, int n) {
        int[] answer;
        if (num_list.length % n == 0) {
            answer = new int[num_list.length / n];
        } else {
            answer = new int[num_list.length / n + 1];
        }

        int idx = 0;
        for (int i = 0; i < num_list.length; i += n) {
            answer[idx] = num_list[i];
            idx++;
        }

        return answer;
    }
}
