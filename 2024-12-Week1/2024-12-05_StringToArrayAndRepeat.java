# https://school.programmers.co.kr/learn/courses/30/lessons/120825

class Solution {
    public String solution(String my_string, int n) {
        String answer = "";
        String[] my_string_ary = new String[my_string.length()];

        for (int i = 0; i < my_string.length(); i++) {
            my_string_ary[i] = String.valueOf(my_string.charAt(i));
        }

        for (String m_s : my_string_ary) {
            answer += m_s.repeat(n);
        }

        return answer;
    }
}
