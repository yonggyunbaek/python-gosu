# https://school.programmers.co.kr/learn/courses/30/lessons/120835

class Solution {
    public int[] solution(int[] emergency) {
        int[] answer = new int[emergency.length];
        
        for(int x=0; x<emergency.length; x++){
            // System.out.println(e);
            int rank = 1;
            for(int y: emergency){
                // System.out.println(y);
                if(emergency[x] < y){
                    rank++;
                }
            }
            answer[x] = rank;
        }
        
        return answer;
    }
}
