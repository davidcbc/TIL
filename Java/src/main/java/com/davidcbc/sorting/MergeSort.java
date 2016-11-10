package com.davidcbc.sorting;

public class MergeSort {
    public void sort(int[] input) {
        if(input.length == 0) return;
        sortHelper(input, 0, input.length);
    }

    private void merge(int[] input, int start, int end) {
        int middle = start+((end-start)/2);
        int[] temp = new int[end-start];
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
    private void sortHelper(int[] input, int start, int end) {
        if(start == end-1) return;
        int middle = start+((end-start)/2);
        sortHelper(input, start, middle);
        sortHelper(input, middle, end);
        merge(input, start, end);
    }
}
