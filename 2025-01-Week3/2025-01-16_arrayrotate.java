# https://school.programmers.co.kr/learn/courses/30/lessons/120844?language=java
class Solution {
    public int[] solution(int[] numbers, String direction) {
        if(direction.equals("right")){
            int last = numbers[numbers.length - 1];
            for (int i = numbers.length - 2; i >= 0; i--) {
                numbers[i + 1] = numbers[i];
            // System.out.println(numbers);
            }
            numbers[0] = last;   
        }
        else{
            int first = numbers[0];
            for (int i = 1; i <= numbers.length -1; i++){
                numbers[i - 1] = numbers[i];
            }
            numbers[numbers.length-1] = first;
        }
        
        return numbers;
    }
}
