# https://school.programmers.co.kr/learn/courses/30/lessons/120861

class Solution {
    public int[] solution(String[] keyinput, int[] board) {
        int[] answer = {0,0};
        int min_x = (board[0]/2)*(-1);
        int max_x = board[0]/2;
        int min_y = (board[1]/2)*(-1);
        int max_y = board[1]/2;
        
        for(String key:keyinput){
            if(key.equals("left")){
                answer[0]--;
            }
            else if(key.equals("right")){
                answer[0]++;
            }
            else if(key.equals("down")){
                answer[1]--;
            }
            else{
                answer[1]++;
            }

            answer[0] = Math.max(min_x, Math.min(max_x, answer[0]));
            answer[1] = Math.max(min_y, Math.min(max_y, answer[1]));
        }
        
        
        return answer;
    }
}
