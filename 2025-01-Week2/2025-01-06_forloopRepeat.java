# https://school.programmers.co.kr/learn/courses/30/lessons/120823

import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        
        for(int num=1; num<=n; num++){
            String star = "*".repeat(num); 
            System.out.println(star);
        }
        // System.out.println(n);
    }
}
