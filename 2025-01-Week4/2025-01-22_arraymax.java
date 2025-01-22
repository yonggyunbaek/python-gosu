# https://school.programmers.co.kr/learn/courses/30/lessons/120862

import java.util.ArrayList;
import java.util.Collections;

class Solution {
    public int solution(int[] numbers) {
        if (numbers.length == 2) {
            return numbers[0] * numbers[1];
        }
        ArrayList<Integer> positive = new ArrayList<>(); 
        ArrayList<Integer> negative = new ArrayList<>();

        for(int num: numbers){
            if(num > 0){
                positive.add(num);
            }
            else if(num < 0){
                negative.add(num);
            }
        }
        Collections.sort(positive);
        Collections.sort(negative);
        
        int max_p = 0;
        int max_n = 0;
        if(positive.size() >= 2){
            int size = positive.size();
            max_p = positive.get(size-1) * positive.get(size-2);
        }
        if(negative.size() >= 2){
            max_n = negative.get(0) * negative.get(1);
        }
        
        if(max_p >= max_n){
            return max_p;
        }
        else{
            return max_n;
        }
    }
}
