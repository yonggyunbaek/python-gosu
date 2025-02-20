# https://school.programmers.co.kr/learn/courses/30/lessons/120913

import java.util.ArrayList;

class Solution {
    public String[] solution(String my_str, int n) {
        ArrayList<String> list = new ArrayList<>();
        int start = 0;
        int end = n;
        
        while(end < my_str.length()){
            list.add(my_str.substring(start, end));
            start = end;
            end += n;
        }
        if(end >= my_str.length()){
            list.add(my_str.substring(start, my_str.length()));
        }

        String[] answer = list.toArray(new String[list.size()]);
        return answer;
    }
}
