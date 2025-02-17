# https://school.programmers.co.kr/learn/courses/30/lessons/120853

import java.util.ArrayList;

class Solution {
    public int solution(String s) {
        int answer = 0;
        ArrayList<String> list = new ArrayList<>();
        
        String[] s_array = s.split(" ");
        for(String str:s_array){
            // System.out.println(str);
            if(str.equals("Z")){
                list.remove(list.size()-1);
            }
            else{
                list.add(str);                
            }
        }
        // System.out.println(list);
        for(String n:list){
            answer += Integer.valueOf(n);
        }
        return answer;
    }
}
