package com.davidcbc.topcoder;

import org.junit.Assert;
import org.junit.Test;

/**
 * Created by David on 11/13/2016.
 */
public class OlympicCandlesTest {

    @Test
    public void testOlympicCandles() {
        OlympicCandles oc = new OlympicCandles();
        int[] input = {2,2,2};
        Assert.assertEquals(3,oc.numberOfNights(input));
    }

    @Test
    public void testOlympicCandles2() {
        OlympicCandles oc = new OlympicCandles();
        int[] input = {2, 2, 2, 4};
        Assert.assertEquals(4,oc.numberOfNights(input));
    }

    @Test
    public void testOlympicCandles3() {
        OlympicCandles oc = new OlympicCandles();
        int[] input = {5, 2, 2, 1};
        Assert.assertEquals(3,oc.numberOfNights(input));
    }

    @Test
    public void testOlympicCandles4() {
        OlympicCandles oc = new OlympicCandles();
        int[] input = {1, 2, 3, 4, 5, 6};
        Assert.assertEquals(6,oc.numberOfNights(input));
    }

    @Test
    public void testOlympicCandles5() {
        OlympicCandles oc = new OlympicCandles();
        int[] input = {1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1};
        Assert.assertEquals(4,oc.numberOfNights(input));
    }
}
