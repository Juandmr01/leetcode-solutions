class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # CREATE empty dictionary called groups
        groups = {}
        
        for word in strs:
            #key = sort the letters of word into a string
            key = "".join(sorted(word))
            # IF key is NOT already in groups:
            if key not in groups:
                # create new empty list at groups[key]
                groups[key] = []
            # ADD word to the list at groups[key]
            groups[key].append(word)
        return list(groups.values())


                

    
    
            

                    