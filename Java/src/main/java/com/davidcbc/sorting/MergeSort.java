package com.davidcbc.sorting;

/**
 * Created by David on 11/9/2016.
 */
public class MergeSort {
    public void sort(int[] input) {
        if(input.length == 0) return;
        sortHelper(input, 0, input.length);
    }

    private void sortHelper(int[] input, int start, int end) {
        if(start == end-1) return;
        int[] temp = new int[end-start];
        int middle = start+((end-start)/2);
        sortHelper(input, start, middle);
        sortHelper(input, middle, end);

        //Merge
        int aPos = start;
        int bPos = middle;
        int i = 0;
        while(aPos < middle || bPos < end) {
            if(aPos == middle) {
                temp[i] = input[bPos++];
            }
            else if(bPos == end) {
                temp[i] = input[aPos++];
            }
            else if(input[aPos] < input[bPos]) {
                temp[i] = input[aPos++];
            }
            else {
                temp[i] = input[bPos++];
            }
            i++;
        }
        for(i = 0; i < temp.length; i++) {
            input[start+i] = temp[i];
        }
    }
}
