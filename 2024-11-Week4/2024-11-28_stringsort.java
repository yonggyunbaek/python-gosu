# https://school.programmers.co.kr/learn/courses/30/lessons/120822
class Solution {
    public String solution(String my_string) {
        String answer = "";

        for(int i=my_string.length()-1 ; i>=0; i--){
            answer += my_string.charAt(i);
        }
        
        return answer;
    }
}

## charAt 함수란?
String 타입의 데이터(문자열)에서 특정 문자를 char 타입으로 변환할 때 사용하는 함수이다.
