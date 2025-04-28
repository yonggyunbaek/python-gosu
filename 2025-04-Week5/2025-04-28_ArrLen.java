# https://school.programmers.co.kr/learn/courses/30/lessons/181856

class Solution {
    public int solution(int[] arr1, int[] arr2) {
        int len1 = arr1.length;
        int len2 = arr2.length;
        int ans1 = 0;
        int ans2 = 0;
        if(len1 < len2){
            return -1;
        }
        else if(len1 > len2){
            return 1;
        }
        else{
            for(int i=0; i<len1;i++){
                ans1 += arr1[i];
                ans2 += arr2[i];
            }
        }
        if(ans1 < ans2){
            return -1;
        }
        else if(ans1 > ans2){
            return 1;
        }
        else{
            return 0;
        }
    }
}
