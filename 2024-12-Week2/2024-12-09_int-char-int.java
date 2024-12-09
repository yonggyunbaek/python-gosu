# https://school.programmers.co.kr/learn/courses/30/lessons/120906

class Solution {
    public int solution(int n) {
        int answer = 0;
        // String str_n = n + "";
        String str_n = Integer.toString(n);
        // System.out.println(str_n);
        char[] str_n_arr = str_n.toCharArray();
        for(char n_char:str_n_arr){
            // Ascii 값을 뺀 결과 반환할 때 숫자로.
            answer += n_char - '0';
        }
        
        return answer;
    }
}
