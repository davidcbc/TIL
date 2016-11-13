package com.davidcbc.topcoder;

/**
 * Created by David on 11/12/2016.
 */
public class ApproximateDivision {
    public double quotient(int a, int b, int terms) {
        int x = b;
        int bits = 0;
        int count = 0;
        while(x > 0) {
            if((x&1)==1)count++;
            x=x>>1;
            bits++;
        }
        if(count == 1) {
            return (double)a/(double)b;
        }
        double t = 1<<bits;
        double c = t-b;
        double value = 0;
        for(int i =0; i < terms; i++) {
            value += ((Math.pow(c,i))/Math.pow(t,i+1));
        }
        return value*a;
    }
}
