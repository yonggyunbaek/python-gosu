import java.util.*;

class Solution {
    public String solution(String letter) {
        // Morse 코드와 알파벳을 매핑하는 맵 생성
        Map<String, Character> morseMap = new HashMap<>();
        String[] morse = {".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", 
                          ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", 
                          ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."};

        // 'a' 부터 'z'까지 알파벳을 이용해 morseMap에 저장
        for (int i = 0; i < morse.length; i++) {
            morseMap.put(morse[i], (char) ('a' + i));
        }

        // 공백을 기준으로 Morse 코드를 분리
        String[] letterSplit = letter.split(" ");
        
        // StringBuilder를 이용해 최종 결과를 생성
        StringBuilder answer = new StringBuilder();
        
        // Morse 코드로부터 알파벳을 찾고, answer에 추가
        for (String morseCode : letterSplit) {
            answer.append(morseMap.get(morseCode));
        }
        
        return answer.toString();
    }
}
