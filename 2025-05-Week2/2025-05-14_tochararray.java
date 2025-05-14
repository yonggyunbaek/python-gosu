# https://school.programmers.co.kr/learn/courses/30/lessons/181907

class Solution {
    public String solution(String my_string, int n) {
        StringBuilder sb = new StringBuilder();
        char[] tmp = my_string.toCharArray();
        
        for(int i = 0; i < n; i++) {
            sb.append(tmp[i]);
        }
        return sb.toString();
    }
}
