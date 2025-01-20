# https://school.programmers.co.kr/learn/courses/30/lessons/120846

class Solution {
    public static boolean isComposite(int num) {
        if (num <= 1) {
            return false;
        }

        for (int i = 2; i <= Math.sqrt(num); i++) {
            if (num % i == 0) {
                return true;
            }
        }        
        return false;
    }
    
    
    public int solution(int n) {
        int answer = 0;
        for (int i = 1; i <= n; i++) {
            if (isComposite(i)) {
                answer++;
            }
        }
        return answer;
    }
}
