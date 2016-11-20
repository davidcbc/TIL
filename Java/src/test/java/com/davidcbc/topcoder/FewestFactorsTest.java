package com.davidcbc.topcoder;

import org.junit.Assert;
import org.junit.Test;

/**
 * Created by David on 11/20/2016.
 */
public class FewestFactorsTest {

    @Test
    public void testFewestFactors1() {
        FewestFactors f = new FewestFactors();
        int[] digits = {1,2};
        Assert.assertEquals(21,f.number(digits));
    }

    @Test
    public void testFewestFactors2() {
        FewestFactors f = new FewestFactors();
        int[] digits = {6,0};
        Assert.assertEquals(6,f.number(digits));
    }

    @Test
    public void testFewestFactors3() {
        FewestFactors f = new FewestFactors();
        int[] digits = {4,7,4};
        Assert.assertEquals(447,f.number(digits));
    }
    @Test
    public void testFewestFactors4() {
        FewestFactors f = new FewestFactors();
        int[] digits = {1, 3, 7, 9};
        Assert.assertEquals(1973,f.number(digits));
    }

    @Test
    public void testFewestFactors5() {
        FewestFactors f = new FewestFactors();
        int[] digits = {7, 5, 4, 3, 6};
        Assert.assertEquals(36457,f.number(digits));
    }

    @Test
    public void testFewestFactors6() {
        FewestFactors f = new FewestFactors();
        int[] digits = {1,2,4};
        Assert.assertEquals(241,f.number(digits));
    }
}
