# https://school.programmers.co.kr/learn/courses/30/lessons/120813

import java.util.Arrays;

class Solution {
    public int[] solution(int n) {
        int[] answer = new int[0];
        
        for(int i=1; i<=n; i++){
            if(i%2==1){
                answer = addElement(answer, i);
            }
        }
        return answer;
    }
    public static int[] addElement(int[] array, int element) {
        int[] newArray = Arrays.copyOf(array, array.length + 1);
        newArray[array.length] = element;
        return newArray;
    }
}
