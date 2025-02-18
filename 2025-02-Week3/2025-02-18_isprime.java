import java.util.ArrayList;

class Solution {
    public int[] solution(int n) {
        ArrayList<Integer> list = new ArrayList<>();
        for(int i = 2; i <= n; i++){
            boolean isPrimeNumber = true;
            
            for(int j = 2; j <= Math.sqrt(i); j++) {
                if(i%j == 0) {
                    isPrimeNumber = false;
                    break;
                }
            }
            if(isPrimeNumber){
                list.add(i);
            }
        }

        int[] answer = new int[list.size()];
        
        for(int i=0; i<list.size();i++){
            answer[i]=list.get(i);
        }

        return answer;
    }
}
