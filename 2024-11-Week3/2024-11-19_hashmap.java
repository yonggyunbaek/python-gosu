# https://school.programmers.co.kr/learn/courses/30/lessons/120812

import java.util.HashMap;
import java.util.Map;

class Solution {
    public int solution(int[] array) {
        // hashmap = python Dict : key-value 형식
        // map 에 hashmap, treemap 등등이 있음
        Map<Integer, Integer> frequencyMap = new HashMap<>();
        
        // 빈도 수 계산
        // for (int arr : array) 구문은 array 배열의 각 요소를 순회
        for (int arr : array) {
            frequencyMap.put(arr, frequencyMap.getOrDefault(arr, 0) + 1);
        }
        // getOrDefault : frequencyMap(hashmap)에서 arr가 있는지 조회하고 있으면 value반환, 없으면 0으로 할당하고 반환
        // put : value 업데이트
        
        int mode = 0;
        int maxFrequency = 0;
        int countOfMaxFrequency = 0;

        // 최빈값 및 빈도 수 확인
        // entrySet : hashmap변수의 key-value 모두 반환
        // entry가 entrySet을 순환하면서 k-v 루프로 확인
        for (Map.Entry<Integer, Integer> entry : frequencyMap.entrySet()) {
            int frequency = entry.getValue(); // hashmap의 value 반환
            if (frequency > maxFrequency) {
                maxFrequency = frequency;
                mode = entry.getKey();
                countOfMaxFrequency = 1;
            } else if (frequency == maxFrequency) {
                countOfMaxFrequency++;
            }
        }

        // 삼항연산자 : 조건 ? 참일 때의 값 : 거짓일 때의 값
        return countOfMaxFrequency > 1 ? -1 : mode;
    }
}

