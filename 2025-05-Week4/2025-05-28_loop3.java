# https://school.programmers.co.kr/learn/courses/30/lessons/181898

class Solution {
    public int solution(int[] arr, int idx) {
        int answer = -1;
        for(int i=idx;i<arr.length;i++){
            if(arr[i]==1){
                return i;
            }
        }
        return answer;
    }
}
