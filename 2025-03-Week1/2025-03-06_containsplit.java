# https://school.programmers.co.kr/learn/courses/30/lessons/120863

class Solution {
    public String solution(String polynomial) {

        int xTerm = 0;
        int constantTerm = 0;

        for (String term : polynomial.split(" ")) {
            if (term.contains("x")) {

                String coefficient = term.replace("x", "");
                if (coefficient.equals("") || coefficient.equals("+")) {
                    coefficient = "1";
                } else if (coefficient.equals("-")) {
                    coefficient = "-1";
                }
                xTerm += Integer.parseInt(coefficient);
            } else if (!term.equals("+")) {
                constantTerm += Integer.parseInt(term);
            }
        }

        StringBuilder result = new StringBuilder();
        if (xTerm != 0) {
            if (xTerm == 1) {
                result.append("x");
            } else if (xTerm == -1) {
                result.append("-x");
            } else {
                result.append(xTerm).append("x");
            }
        }
        if (constantTerm != 0) {
            if (result.length() > 0) {
                result.append(" + ");
            }
            result.append(constantTerm);
        }

        return result.length() > 0 ? result.toString() : "0";
    }
}
