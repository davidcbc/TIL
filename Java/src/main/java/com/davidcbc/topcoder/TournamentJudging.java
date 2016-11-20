package com.davidcbc.topcoder;

/**
 * Created by David on 11/15/2016.
 */
public class TournamentJudging {
    public int getPoints(int[] rawScores, int[] conversionFactor) {
        int points = 0;
        for(int i =0; i < rawScores.length; i++) {
            points += Math.round(((float)rawScores[i]/(float)conversionFactor[i]));
        }
        return points;
    }
}
