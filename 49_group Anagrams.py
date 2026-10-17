class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        
        for i in range(len(strs)):
            for j in range(i +1, len(strs)):
               if (sorted(strs[i]) == sorted(strs[j])):
                    strs.extend([i, j])
        print(strs)