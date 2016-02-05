/*
 * Problem Statement:
 * Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).
 * For example, the 32-bit integer '11' has binary representation 00000000000000000000000000001011, so the function should return 3.
 * 
 * Test cases passed: 600/600
 * Runtime: 4 ms
 * 
 */
int hammingWeight(uint32_t n) {
    
    
    int numOnes = 0; //count of 1 bits
    int MASK = 1;  //bit mask
   
    while (n) { //keep looping through the bits of n
        if (n & MASK){ //if bitwise AND of n and MASK is 1, increment the amount of 1 bits
            numOnes++;
        }
        
        n >>= 1; //shift n to check next bit
            
    }
    
    return numOnes;
}