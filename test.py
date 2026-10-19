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
                group[key] = 0    
            group[key] += 1       
        top = sorted(group.items(), key=lambda x: x[1], reverse=True)[:k]
        return [item[0] for item in top]
    
    ## reutnr 
 
            
        