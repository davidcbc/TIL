package com.davidcbc.leetcode;

public class LC3 {

    //Length of longest substring without repeating characters
    public int lengthOfLongestSubstring(String s) {
        char[] c = s.toCharArray();
        int max = 0;
        for(int i = 0; i < c.length; i++) {
            boolean[] seen = new boolean[128];
            int count = 0;
            for(int j = i; j < c.length; j++) {
                if(seen[c[j]]) {
                    break;
                }
                else {
                    seen[c[j]] = true;
                    count++;
                }
            }
            if(count > max) {
                max = count;
            }
        }
        return max;
    }
}
