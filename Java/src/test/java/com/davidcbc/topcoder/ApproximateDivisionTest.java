package com.davidcbc.topcoder;

import org.junit.Assert;
import org.junit.Test;

/**
 * Created by David on 11/12/2016.
 */
public class ApproximateDivisionTest {

    @Test
    public void testApproximateDivision() {
        ApproximateDivision toTest = new ApproximateDivision();
        Assert.assertEquals(0.34375, toTest.quotient(2,5,2),0);
    }

    @Test
    public void testApproximateDivisionPower2() {
        ApproximateDivision toTest = new ApproximateDivision();
        Assert.assertEquals(0.875, toTest.quotient(7,8,5),0);
    }

    @Test
    public void testApproximateDivisionLargeB() {
        ApproximateDivision toTest = new ApproximateDivision();
        Assert.assertEquals(8.481740951538086E-5, toTest.quotient(1,10000,2),0);
    }
}
