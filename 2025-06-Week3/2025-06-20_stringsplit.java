# https://school.programmers.co.kr/learn/courses/30/lessons/181926

class Solution {
    public int solution(int n, String control) {
        int answer = n;
        String[] words = control.split("");
        for (String word : words) {
            if (word.equals("w")) {
                answer++;
            } else if (word.equals("s")) {
                answer--;
            } else if (word.equals("d")) {
                answer += 10;
            } else if (word.equals("a")) {
                answer -= 10;
            }
        }
        return answer;
    }
}
