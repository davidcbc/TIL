package com.davidcbc.topcoder;

import java.util.Arrays;

/**
 * Created by David on 11/13/2016.
 */
public class DNAString {
    public int minChanges(int maxPeriod, String[] dna) { //O(maxPeriod^2 + maxPeriod*N)
        int[] minChanges = new int[maxPeriod+1];
        Arrays.fill(minChanges,Integer.MAX_VALUE);
        String dnaCombo = combineStrings(dna);
        for(int i = 1; i <= maxPeriod; i++) { // O(maxPeriod)
            //Find minimum changes
            int changes = getMinimumChanges(dnaCombo, i); //O(maxPeriod + N)
            if(changes < minChanges[i]) {
                minChanges[i] = changes;
            }
        }
        int overallMin = Integer.MAX_VALUE;
        for(int i = 0; i < minChanges.length; i++) { // O(maxPeriod)
            if(minChanges[i] < overallMin) {
                overallMin = minChanges[i];
            }
        }
        return overallMin;
    }


    public int getMinimumChanges(String dna, int period) { //O(period + N)
        int changes = 0;
        for(int i = 0; i < period; i++) { // O(period)
            int[] charCounts = new int[4];
            int total = 0;
            for(int j = i; j < dna.length(); j+=period) { //O(N) only look at each character once
                charCounts[dnaToInt(dna.charAt(j))]++;
                total++;
            }
            int max = Integer.MIN_VALUE;
            for(int j = 0; j < charCounts.length; j++) { //O(4)
                if(charCounts[j] > max) {
                    max = charCounts[j];
                }
            }
            changes += (total-max);
        }
        return changes;
    }

    private int dnaToInt(char dna) {
        switch(dna) {
            case 'A': return 0;
            case 'C': return 1;
            case 'G': return 2;
            case 'T': return 3;
            default: return -1;
        }
    }

    private String combineStrings(String[] dna) {
        StringBuilder sb = new StringBuilder();
        for(String s : dna) {
            sb.append(s);
        }
        return sb.toString();
    }
}
