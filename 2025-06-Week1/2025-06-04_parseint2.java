# https://school.programmers.co.kr/learn/courses/30/lessons/181939

class Solution {
    public int solution(int a, int b) {
        int answer = 0;
        if((Integer.parseInt(""+a+b))>=(Integer.parseInt(""+b+a))){
            return Integer.parseInt(""+a+b);
        }
        else{
            return Integer.parseInt(""+b+a);
        }
    }
}
