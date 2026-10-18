class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # create a dictionary wiht Key and values 
        group = {}
        #for each value in nums
        for number in nums:
            key = number 
            if number not in group:
                group[key] = []
                group[key] += 1
            else: group[key] += 1
            print("value")       
        return max(group, key=group.get)
 
            
        