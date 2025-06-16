# https://school.programmers.co.kr/learn/courses/30/lessons/181915

class Solution {
    public String solution(String my_string, int[] index_list) {
        String[] str = my_string.split("");
        String answer = "";
        for(int idx:index_list){
            answer += str[idx];
        }

        return answer;
    }
}
