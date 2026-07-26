class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Convert the nums to set 
        # Find the start of the sequence 
        # Then use while loop to find the longest sequence
        if not nums:
            return 0 
        setNums = set(nums)
        finalLongest = 1

        for num in setNums:
            # Check if start of the sequence
            # We can do this using the idea to check if num - 1 in setNums 
            if (num - 1) not in setNums:
                start = num
                longest = 1
                while (start + 1) in setNums:
                    longest += 1
                    start += 1
            
                finalLongest = max(longest, finalLongest)
        
        return finalLongest
