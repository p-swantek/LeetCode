import java.util.Arrays;

/*
 * Problem Statement:
 * Given an array of integers, find if the array contains any duplicates. 
 * Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.
 * 
 * Test cases passed: 16/16
 * Runtime: 6 ms
 * 
 */
public class ContainsDuplicate {
	
	public boolean containsDuplicate(int[] nums) {
	        
	        if (nums.length == 0)
	            return false;
	        
	        Arrays.sort(nums);
	        
	        for (int i = 0; i < nums.length-1; i++){
	            if (nums[i] == nums[i+1]){
	                return true;
	            }
	        }
	        
	        return false;
	        
	    }

}
