package com.davidcbc.topcoder;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

/**
 * Created by David on 11/20/2016.
 */
public class FewestFactors {
    public int number(int[] digits) {
        List<List<Integer>> permutations = new ArrayList<>();
        boolean[] visited = new boolean[digits.length];
        createPermutations(digits, visited, permutations, new ArrayList<>());
        List<Integer> combinedPermutations = new ArrayList<>();
        for(List<Integer> list : permutations) {
            int value = 0;
            for(int i : list) {
                value *= 10;
                value += i;
            }
            combinedPermutations.add(value);
        }
        int minFactors = Integer.MAX_VALUE;
        int minNumber = 0;
        for(int i : combinedPermutations) {
            int factors = 0;
            for(int j = 1; j < Math.sqrt(i); j++) {
                factors += i%j==0 ? 1 : 0;
            }
            if(factors < minFactors) {
                minFactors = factors;
                minNumber = i;
            }
            else if(factors == minFactors) {
                if(minNumber > i) {
                    minNumber = i;
                }
            }
        }
        return minNumber;
    }

    public void createPermutations(int[] digits, boolean[] visited, List<List<Integer>> list, List<Integer> tempList) {
        boolean finished = true;
        for(int i = 0; i < digits.length; i++) {
            if(!visited[i]) {
                finished=false;
                tempList.add(digits[i]);
                visited[i] = true;
                createPermutations(digits,visited,list,tempList);
                visited[i] = false;
                tempList.remove(tempList.size()-1);
            }
        }
        if(finished) {
            list.add(new ArrayList<>(tempList));
        }
    }
}
