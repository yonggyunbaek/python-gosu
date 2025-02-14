# https://school.programmers.co.kr/learn/courses/30/lessons/120912

class Solution {
    public int solution(int[] array) {
        int answer = 0;
        for(int num: array){
            String strNum = String.valueOf(num);
            for (char n : strNum.toCharArray()) {
                if (n == '7') {
                    answer++;
                }
            }
        }
        return answer;
    }
}
