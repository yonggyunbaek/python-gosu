# https://school.programmers.co.kr/learn/courses/30/lessons/181910

class Solution {
    public String solution(String my_string, int n) {
        int index = my_string.length() - n;
        return my_string.substring(index);
    }
}
