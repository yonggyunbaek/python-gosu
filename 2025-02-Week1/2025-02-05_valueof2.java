# https://school.programmers.co.kr/learn/courses/30/lessons/120904

class Solution {
    public int solution(int num, int k) {
        int answer = 0;
        String string_num = String.valueOf(num);
        
        for(int i=0; i<string_num.length(); i++){
            int cur_num = Character.getNumericValue(string_num.charAt(i));
            if (cur_num == k){
                answer=i+1;
                break;
            }
        }
        if(answer==0){
            return -1;
        }
        else{
            return answer;            
        }
    }
}
