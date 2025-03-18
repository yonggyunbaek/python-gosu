# https://school.programmers.co.kr/learn/courses/30/lessons/120878

class Solution {
    public int solution(int a, int b) {
        int gcd = gcd(a, b);
        b /= gcd;

        while (b % 2 == 0) {
            b /= 2;
        }
        while (b % 5 == 0) {
            b /= 5;
        }

        return (b == 1) ? 1 : 2;
    }

    private int gcd(int x, int y) {
        while (y != 0) {
            int temp = y;
            y = x % y;
            x = temp;
        }
        return x;
    }
}
