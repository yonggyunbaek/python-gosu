# https://github.com/yonggyunbaek/python-gosu/blob/main/2025-05-Week2/2025-05-16_upper.java

class Solution {
    public int solution(String myString, String pat) {
        String myString_low = myString.toLowerCase();
        String pat_low = pat.toLowerCase();
        if(myString_low.contains(pat_low)){
            return 1;
        }
        else{
            return 0;
        }
    }
}
