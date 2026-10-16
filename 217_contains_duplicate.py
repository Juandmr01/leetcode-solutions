## Contains Duplicate

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
   
        ## it sort all the variable  i have and delete duplicates
        seen = []
        # do a loop in my listt
        for i in nums:
            # check if the varaible is in seen
            if i in seen:
                return True
            # if not seen it, it add it in our variable
            seen[i]
        # retrun do go to other index
        return False
        
        seen2 = set()
          # do a loop in my listt
        for i in numss:
            # check if the varaible is in seen
            if i in seen2:
                return True
            # if not seen it, it add it in our variable
            seen.add(i)
        # retrun do go to other index
        return False

                

            