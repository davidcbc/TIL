package com.davidcbc.topcoder;

import org.junit.Assert;
import org.junit.Test;

/**
 * Created by David on 11/13/2016.
 */
public class DNAStringTest {
    @Test
    public void testDNAString() {
        DNAString dna = new DNAString();
        String[] input =  {"ATAGATA"};
        Assert.assertEquals(1,dna.minChanges(3,input));
    }

    @Test
    public void testDNAString2() {
        DNAString dna = new DNAString();
        String[] input = {"ACGTGCA"};
        Assert.assertEquals(3, dna.minChanges(2,input));
    }

    @Test
    public void testDNAString3() {
        DNAString dna = new DNAString();
        String[] input = {"ACGCTGACAGATA"};
        Assert.assertEquals(0, dna.minChanges(13,input));
    }

    @Test
    public void testDNAString4() {
        DNAString dna = new DNAString();
        String[] input = {"AAAATTTCCG"};
        Assert.assertEquals(6, dna.minChanges(1,input));
    }

    @Test
    public void testDNAString5() {
        DNAString dna = new DNAString();
        String[] input = {"ACGTATAGCATGACA","ACAGATATTATG","ACAGATGTAGCAGTA","ACCA","GAC"};
        Assert.assertEquals(20, dna.minChanges(12,input));
    }

}
