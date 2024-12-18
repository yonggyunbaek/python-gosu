# https://school.programmers.co.kr/learn/courses/30/lessons/120889
import java.util.Arrays;
    
class Solution {
    public int solution(int[] sides) {
        Arrays.sort(sides);
        // System.out.println(sides[0]);
        if(sides[0]+sides[1] > sides[2]){
            return 1;
        }
        else{
            return 2;
        }
    }
}
