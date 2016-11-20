package com.davidcbc.topcoder;

import org.junit.Assert;
import org.junit.Test;

/**
 * Created by David on 11/20/2016.
 */
public class PrimeStatisticsTest {
    @Test
    public void primeStatisticsTest1() {
        PrimeStatistics ps = new PrimeStatistics();
        Assert.assertEquals(3, ps.mostCommonRemainder(3,14,5));
    }

    @Test
    public void primeStatisticsTest2() {
        PrimeStatistics ps = new PrimeStatistics();
        Assert.assertEquals(3, ps.mostCommonRemainder(3,33,1000));
    }

    @Test
    public void primeStatisticsTest3() {
        PrimeStatistics ps = new PrimeStatistics();
        Assert.assertEquals(0, ps.mostCommonRemainder(25,27,17));
    }

    @Test
    public void primeStatisticsTest4() {
        PrimeStatistics ps = new PrimeStatistics();
        Assert.assertEquals(1, ps.mostCommonRemainder(1,200000,2));
    }

    @Test
    public void primeStatisticsTest5() {
        PrimeStatistics ps = new PrimeStatistics();
        Assert.assertEquals(5, ps.mostCommonRemainder(1,1000,6));
    }
}
