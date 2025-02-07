# https://school.programmers.co.kr/learn/courses/30/lessons/120887
class Solution {
    public int solution(int i, int j, int k) {
        int answer = 0;
        for(int num=i; num<=j; num++){
            String numStr = Integer.toString(num);
            for (char c : numStr.toCharArray()) {
                if(k==c-'0'){
                    answer++;
                }
            }
        }
        
        return answer;
    }
}
