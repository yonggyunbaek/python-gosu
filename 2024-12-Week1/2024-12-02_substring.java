# https://school.programmers.co.kr/learn/courses/30/lessons/120908

class Solution {
    public int solution(String str1, String str2) {
        int answer = 2;
        char[] str1_arr = str1.toCharArray();
        char str2_s = str2.charAt(0);

        int str1_len = str1.length();
        int str2_len = str2.length();

        for (int i = 0; i <= str1_len - str2_len; i++) {
            if (str1_arr[i] == str2_s) {
                if (str1.substring(i, i + str2_len).equals(str2)) {
                    return answer = 1;
                }
            }
        }

        return answer;
    }
}
