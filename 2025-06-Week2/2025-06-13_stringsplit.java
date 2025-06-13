# https://school.programmers.co.kr/learn/courses/30/lessons/181914

class Solution {
    public int solution(String number) {
        String[] words = number.split("");
        int n = 0;
        for(String word : words){
            n += Integer.parseInt(word);
        }
        return n % 9;
    }
}
