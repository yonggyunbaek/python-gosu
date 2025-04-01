# https://school.programmers.co.kr/learn/courses/30/lessons/181933 
class Solution {
    public int solution(int a, int b, boolean flag) {
        int answer = 0;
        if(flag){
            return a+b;
        }
        else{
            return a-b;
        }
    }
}
