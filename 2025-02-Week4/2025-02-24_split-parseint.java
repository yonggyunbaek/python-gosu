# https://school.programmers.co.kr/learn/courses/30/lessons/120902?language=java

class Solution {
    public int solution(String my_string) {
        String[] tokens = my_string.split(" ");
        int result = 0;
        int sign = 1;

        for (String token : tokens) {
            if (token.equals("+")) {
                sign = 1;
            } else if (token.equals("-")) {
                sign = -1;
            } else {
                result += sign * Integer.parseInt(token);
            }
        }

        return result;
    }
}
