# https://school.programmers.co.kr/learn/courses/30/lessons/181906
class Solution {
    public int solution(String my_string, String is_prefix) {
        if (my_string.startsWith(is_prefix)) {
            return 1;
        } else {
            return 0;
        }
    }
}
