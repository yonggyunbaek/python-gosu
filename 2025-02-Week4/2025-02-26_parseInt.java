# https://school.programmers.co.kr/learn/courses/30/lessons/120907

import java.util.*;

class Solution {
    public String[] solution(String[] quiz) {
        String[] result = new String[quiz.length];
        
        for (int i = 0; i < quiz.length; i++) {
            String[] parts = quiz[i].split(" ");
            
            int X = Integer.parseInt(parts[0]);
            String operator = parts[1];
            int Y = Integer.parseInt(parts[2]);
            int Z = Integer.parseInt(parts[4]);

            int calculated = operator.equals("+") ? (X + Y) : (X - Y);
            result[i] = (calculated == Z) ? "O" : "X";
        }
        
        return result;
    }
}
