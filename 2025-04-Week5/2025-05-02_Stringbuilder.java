# https://school.programmers.co.kr/learn/courses/30/lessons/181863

class Solution {
    public String solution(String rny_string) {
        StringBuilder sb = new StringBuilder();
        
        for(char str:rny_string.toCharArray()){
            if(str=='m'){
                sb.append("rn");
            }
            else{
                sb.append(str);
            }
        }
        
        return sb.toString();
    }
}
