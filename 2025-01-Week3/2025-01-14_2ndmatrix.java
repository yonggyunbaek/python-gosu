# https://school.programmers.co.kr/learn/courses/30/lessons/120842
class Solution {
    public int[][] solution(int[] num_list, int n) {
        int x = num_list.length/n;
        int[][] answer = new int[x][n];
        
        int num = 0;
        for(int j=0; j<x; j++){
            for(int i=0; i<n;i++){
                answer[j][i]=num_list[num];
                num++;
            }
        }
        
        return answer;
    }
}
