# https://school.programmers.co.kr/learn/courses/30/lessons/181901

class Solution {
    public int[] solution(int n, int k) {
        int[] answer = new int[n/k];
        int idx = 0;
        for(int i=k;i<=n;i+=k){
            answer[idx] = i;
            idx++;
        }
        return answer;
    }
}
