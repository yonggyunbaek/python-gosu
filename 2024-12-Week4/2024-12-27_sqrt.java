# https://school.programmers.co.kr/learn/courses/30/lessons/120909

class Solution {
    public int solution(int n) {
        // double num = Math.sqrt(n);
        long num = (long)Math.sqrt(n);
        // System.out.println(num);
        if (n == Math.pow(num, 2)){
            return 1;
        }
        else{
            return 2;
        }
    }
}
