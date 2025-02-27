# https://school.programmers.co.kr/learn/courses/30/lessons/120860

class Solution {
    public int solution(int[][] dots) {
        int minX = Integer.MAX_VALUE, maxX = Integer.MIN_VALUE;
        int minY = Integer.MAX_VALUE, maxY = Integer.MIN_VALUE;

        for (int[] dot : dots) {
            minX = Math.min(minX, dot[0]);
            maxX = Math.max(maxX, dot[0]);
            minY = Math.min(minY, dot[1]);
            maxY = Math.max(maxY, dot[1]);
        }

        int width = maxX - minX;
        int height = maxY - minY;

        return width * height;
    }
}
