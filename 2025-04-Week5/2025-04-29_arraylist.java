# https://school.programmers.co.kr/learn/courses/30/lessons/181861

import java.util.ArrayList;

class Solution {
    public int[] solution(int[] arr) {
        ArrayList<Integer> list = new ArrayList<Integer>();
        for (int a : arr) {
            for (int i = 0; i < a; i++) {
                list.add(a);
            }
        }
        int[] answer = new int[list.size()];
        for (int i = 0; i < list.size(); i++) {
            answer[i] = list.get(i);
        }
        return answer;
    }
}
