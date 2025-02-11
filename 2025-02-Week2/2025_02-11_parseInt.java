# https://school.programmers.co.kr/learn/courses/30/lessons/120864

class Solution {
    public int solution(String my_string) {
        int answer = 0;
        StringBuilder sb = new StringBuilder();
        
        for (char c : my_string.toCharArray()) {
            if (Character.isDigit(c)) {
                sb.append(c);
            } else {
                if (sb.length() > 0) {
                    answer += Integer.parseInt(sb.toString());
                    sb.setLength(0);
                }
            }
        }

        if (sb.length() > 0) {
            answer += Integer.parseInt(sb.toString());
        }
        
        return answer;
    }
}
