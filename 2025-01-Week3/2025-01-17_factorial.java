# https://school.programmers.co.kr/learn/courses/30/lessons/120848
class Solution {
    public int solution(int n) {
        
        for(int i=1; i<=10;i++){
            int tmp = 1;
            for(int x=i; x>0; x--){
                tmp *= x;
            }
            if(tmp>n){
                return i-1;
            }
        }
        return 10;
    }
}
