package com.davidcbc.sorting;

import com.davidcbc.sorting.MergeSort;
import org.junit.*;
/**
 * Created by David on 11/9/2016.
 */
public class MergeSortTest {
    MergeSort sort;

    @Test
    public void testSimpleMergeSortEven() {
        sort = new MergeSort();
        int[] input = {2,1};
        sort.sort(input);
        int[] expected = {1,2};
        Assert.assertArrayEquals(expected, input);
    }

    @Test
    public void testSimpleMergeSortOdd() {
        sort = new MergeSort();
        int[] input = {2,1,5};
        sort.sort(input);
        int[] expected = {1,2,5};
        Assert.assertArrayEquals(expected, input);
    }

    @Test
    public void testEmptyMergeSort() {
        sort = new MergeSort();
        int[] input = {};
        sort.sort(input);
        int[] expected = {};
        Assert.assertArrayEquals(expected, input);
    }

    @Test
    public void testSingleMergeSort() {
        sort = new MergeSort();
        int[] input = {5};
        sort.sort(input);
        int[] expected = {5};
        Assert.assertArrayEquals(expected, input);
    }

    @Test
    public void testMultipleMergeSort() {
        sort = new MergeSort();
        int[] input = {5,10,65,1, -10, 15, 29, 159, 12, 14, 18, 2000, -10000};
        sort.sort(input);
        int[] expected = {-10000, -10, 1, 5, 10, 12, 14, 15, 18, 29, 65,159, 2000};
        Assert.assertArrayEquals(expected, input);
    }
}
