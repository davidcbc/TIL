package com.davidcbc.topcoder;

import java.util.*;

/**
 * Created by David on 11/13/2016.
 */
public class OlympicCandles {
    public int numberOfNights(int[] candles) {
        //While there are a enough candles
        //Subtract 1 from the biggest candle d times, can't light same candle twice;
        Queue<Integer> pQueue = new PriorityQueue<>((Integer o1, Integer o2)->o2-o1);
        for(int candle : candles) {
            pQueue.add(candle);
        }
        int count = 0;
        while(true) {
            List<Integer> usedCandles = new ArrayList<>(count+1);
            if(pQueue.size() < count+1) {
                return count;
            }
            count++;
            for(int i = 0; i < count; i++) {
                int candle = pQueue.poll()-1;
                if(candle>0) {
                    usedCandles.add(candle);
                }
            }
            pQueue.addAll(usedCandles);
        }
    };
}
