# https://school.programmers.co.kr/learn/courses/30/lessons/181925

class Solution {
    public String solution(int[] numLog) {
        String answer = "";
        int tmp = numLog[0];
        
        for(int i=1; i<numLog.length;i++){
            // System.out.println(numLog[i]);
            if(tmp-numLog[i]==-1){
                answer+="w";
            }
            else if(tmp-numLog[i]==1){
                answer+="s";
            }
            else if(tmp-numLog[i]==-10){
                answer+="d";
            }
            else{
                answer+="a";
            }
            tmp = numLog[i];
        }
        return answer;
    }
}
