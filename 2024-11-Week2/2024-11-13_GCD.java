# https://school.programmers.co.kr/learn/courses/30/lessons/120808

class Solution {
    public int[] solution(int numer1, int denom1, int numer2, int denom2) {
        int numerator = (numer1 * denom2) + (numer2 * denom1);
        int denominator = denom1 * denom2;
        
        int divisor = gcd(numerator, denominator);
        
        int[] answer = new int[] {numerator / divisor, denominator / divisor};
        
        return answer;
    }
    public static int gcd(int a, int b) {
        while (b != 0) {
            int temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    }
}

