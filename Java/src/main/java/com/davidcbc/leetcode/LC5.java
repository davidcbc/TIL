package com.davidcbc.leetcode;

/**
 * Created by David on 11/13/2016.
 */
public class LC5 {
    Integer[][] memo;
    int maxI = 0;
    int maxJ = 0;
    int max = 0;
    public String longestPalindrome(String s) {
        if(new StringBuilder(s).reverse().toString().equals(s)) {
            return s;
        }
        if(s.length() == 1) {
            return s;
        }
        memo = new Integer[s.length()][s.length()];
        for(int i = 0; i < s.length(); i++) {
            findLongestPalindrome(s,i,i+1);
            findLongestPalindrome(s,i,i+2);
        }
        return s.substring(maxI, maxJ+1);
    }

    private int findLongestPalindrome(String s, int l, int r) {
        if(l < 0 || r > s.length() || s.charAt(l) != s.charAt(r-1)) {
            return 0;
        }
        if(memo[l][r-1] != null) {
            return memo[l][r-1];
        }
        int bothSides = findLongestPalindrome(s, l-1, r+1);
        memo[l][r-1] = bothSides > (r-l) ? bothSides : (r-l);
        if(memo[l][r-1] > max) {
            maxI = l;
            maxJ = r-1;
            max = memo[l][r-1];
        }
        return memo[l][r-1];
    }
}
