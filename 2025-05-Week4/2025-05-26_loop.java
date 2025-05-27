# https://school.programmers.co.kr/learn/courses/30/lessons/181886

class Solution {
    public String[] solution(String[] names) {
        String[] answer = new String[(names.length + 4) / 5];
        int idx = 0;
        for (int i = 0; i < names.length; i += 5) {
            answer[idx] = names[i];
            idx++;
        }
        return answer;
    }
}
