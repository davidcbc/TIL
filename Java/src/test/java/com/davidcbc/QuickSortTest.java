package com.davidcbc;

import com.davidcbc.sorting.QuickSort;
import org.junit.Assert;
import org.junit.Test;

public class QuickSortTest {
    QuickSort sort;

    @Test
    public void testSimpleQuickSortEven() {
        sort = new QuickSort();
        int[] input = {2,1};
        sort.sort(input);
        int[] expected = {1,2};
        Assert.assertArrayEquals(expected, input);
    }

    @Test
    public void testSimpleQuickSortOdd() {
        sort = new QuickSort();
        int[] input = {2,1,5};
        sort.sort(input);
        int[] expected = {1,2,5};
        Assert.assertArrayEquals(expected, input);
    }

    @Test
    public void testEmptyQuickSort() {
        sort = new QuickSort();
        int[] input = {};
        sort.sort(input);
        int[] expected = {};
        Assert.assertArrayEquals(expected, input);
    }

    @Test
    public void testSingleQuickSort() {
        sort = new QuickSort();
        int[] input = {5};
        sort.sort(input);
        int[] expected = {5};
        Assert.assertArrayEquals(expected, input);
    }

    @Test
    public void testMultipleQuickSort() {
        sort = new QuickSort();
        int[] input = {5, 10, 65, 1, -10, 15, 29, 159, 12, 14, 18, 2000, -10000};
        sort.sort(input);
        int[] expected = {-10000, -10, 1, 5, 10, 12, 14, 15, 18, 29, 65,159, 2000};
        Assert.assertArrayEquals(expected, input);
    }
}
