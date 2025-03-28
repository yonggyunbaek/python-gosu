# https://school.programmers.co.kr/learn/courses/30/lessons/181944

import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        
        if(n%2==0){
            String out = n +" is even";
            System.out.println(out);
        }
        else{
            String out = n +" is odd";
            System.out.println(out);
        }
    }
}
