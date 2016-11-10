package com.davidcbc.sorting;

import java.util.Random;

public class QuickSort {
    static int calls = 0;
    public void sort(int[] input) {
        sortHelper(input, 0, input.length);
    }

    private void sortHelper(int[] input, int start, int end) {
        if(start >= end - 1) return;
        Random rand = new Random();
        int index = rand.nextInt(end-start)+start;
        int pivot = input[index];
        int i = start;
        int j = end-1;
        while(i < j) {
            while(input[i] < pivot) {
                i++;
            }
            while(input[j] > pivot) {
                j--;
            }
            if(i < j) {
                int temp = input[i];
                input[i] = input[j];
                input[j] = temp;
            }
        }
        sortHelper(input, start, j);
        sortHelper(input, i, end);
    }
}
