package com.davidcbc.topcoder;

import org.junit.Assert;
import org.junit.Test;

/**
 * Created by David on 11/15/2016.
 */
public class TournamentJudgingTest {
    @Test
    public void testTournamentJudging1() {
        TournamentJudging toTest = new TournamentJudging();
        int[] scores = {10,20,30};
        int[] conversion = {10,10,5};
        Assert.assertEquals(9,toTest.getPoints(scores,conversion));
    }

    @Test
    public void testTournamentJudging2() {
        TournamentJudging toTest = new TournamentJudging();
        int[] scores = {8,16,32};
        int[] conversion = {10,10,5};
        Assert.assertEquals(9,toTest.getPoints(scores,conversion));
    }

    @Test
    public void testTournamentJudging3() {
        TournamentJudging toTest = new TournamentJudging();
        int[] scores = {60,59};
        int[] conversion = {24,24};
        Assert.assertEquals(5,toTest.getPoints(scores,conversion));
    }

    @Test
    public void testTournamentJudging4() {
        TournamentJudging toTest = new TournamentJudging();
        int[] scores = {47, 42, 37, 30, 27, 21, 18};
        int[] conversion = {1, 2, 3, 4, 5, 6, 7};
        Assert.assertEquals(100, toTest.getPoints(scores,conversion));
    }

    @Test
    public void testTournamentJudging5() {
        TournamentJudging toTest = new TournamentJudging();
        int[] scores = {0, 1000000, 5000, 1000000};
        int[] conversion = {1, 2, 1000000, 4};
        Assert.assertEquals(750000, toTest.getPoints(scores,conversion));
    }
}
