# https://school.programmers.co.kr/learn/courses/30/lessons/120882

import java.util.Arrays;
import java.util.Comparator;

class Solution {
    public int[] solution(int[][] score) {
        int n = score.length;
        double[] avg_score = new double[n];
        Integer[] index = new Integer[n];
        
        for (int i = 0; i < n; i++) {
            avg_score[i] = (score[i][0] + score[i][1]) / 2.0; 
            index[i] = i;
        }

        Arrays.sort(index, (a, b) -> Double.compare(avg_score[b], avg_score[a]));

        int[] ranks = new int[n];
        int rank = 1; 

        for (int i = 0; i < n; i++) {
            if (i > 0 && avg_score[index[i]] == avg_score[index[i - 1]]) {
                ranks[index[i]] = ranks[index[i - 1]];
            } else {
                ranks[index[i]] = rank;
            }
            rank++;
        }

        return ranks;
    }
}
