# https://school.programmers.co.kr/learn/courses/30/lessons/181947

import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        int sum = a + b;
        // System.out.println(a + b);

        String answer = a + " + " + b + " = " + sum;
        System.out.println(answer);
    }
}
