# https://school.programmers.co.kr/learn/courses/30/lessons/120866

class Solution {
    public int solution(int[][] board) {
        int n = board.length;
        int[][] dangerZone = new int[n][n];
        int[] dx = {-1, -1, -1, 0, 1, 1, 1, 0};
        int[] dy = {-1, 0, 1, 1, 1, 0, -1, -1};

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (board[i][j] == 1) {
                    dangerZone[i][j] = 1;
                    for (int k = 0; k < 8; k++) {
                        int ni = i + dx[k];
                        int nj = j + dy[k];
                        if (ni >= 0 && ni < n && nj >= 0 && nj < n) {
                            dangerZone[ni][nj] = 1;
                        }
                    }
                }
            }
        }


        int answer = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (dangerZone[i][j] == 0) {
                    answer++;
                }
            }
        }

        return answer;
    }
}
