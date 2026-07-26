class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Loop through all of them, sort and add them to dic 
        dic = {}

        for s in strs:
            sorted_word = ''.join(sorted(s))
            if sorted_word not in dic:
                dic[sorted_word] = [s]
            else:
                dic[sorted_word].append(s)
        
        return list(dic.values())
