# https://school.programmers.co.kr/learn/courses/30/lessons/120883
class Solution {
    public String solution(String[] id_pw, String[][] db) {
        String answer = "fail";
        for(String[] check: db){
            System.out.println(check);
            if(id_pw[0].equals(check[0]) && id_pw[1].equals(check[1])){
                answer = "login";
            }
            else if(id_pw[0].equals(check[0]) && !id_pw[1].equals(check[1])){
                answer = "wrong pw";
            }
            else{
                continue;
            }
        }
        return answer;
    }
}
