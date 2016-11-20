package com.davidcbc.topcoder;

import java.util.Arrays;

/**
 * Created by David on 11/20/2016.
 */
public class PrimeStatistics {
    public int mostCommonRemainder(int lowerBound, int upperBound, int modulo) {
        boolean[] primes = new boolean[upperBound+1];
        int[] remainders = new int[modulo];
        int maxRemainder = 0;
        int remainderValue = 0;
        Arrays.fill(primes, true);
        for(int i = 2; i <= upperBound; i++) {
            if (primes[i]) {
                for (int j = i + i; j <= upperBound; j += i) {
                    primes[j] = false;
                }
                if (i >= lowerBound) {
                    remainders[i % modulo]++;
                    if(remainders[i%modulo] > maxRemainder) {
                        maxRemainder = remainders[i%modulo];
                        remainderValue = i%modulo;
                    }
                }
            }
        }
        return remainderValue;
    }
}
