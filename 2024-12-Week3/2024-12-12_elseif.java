# https://school.programmers.co.kr/learn/courses/30/lessons/120818

class Solution {
    public int solution(int price) {
        if (price >= 500000) {
            price = (int)(price * 0.8);
        } else if (price >= 300000) {
            price = (int)(price * 0.9);
        } else if (price >= 100000) {
            price = (int)(price * 0.95);
        }
        return price;
    }
}
