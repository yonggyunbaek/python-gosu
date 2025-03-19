# https://school.programmers.co.kr/learn/courses/30/lessons/120921

class Solution {
    public int solution(String A, String B) {
        if (A.equals(B)) {
            return 0;
        }
        
        String temp = A;
        int len = A.length();
        
        for (int i = 1; i < len; i++) {
            temp = temp.charAt(len - 1) + temp.substring(0, len - 1);
            if (temp.equals(B)) {
                return i;
            }
        }
        
        return -1;
    }
}
