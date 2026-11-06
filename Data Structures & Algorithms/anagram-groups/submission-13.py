class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Sorting is a way to do this but not the only way 
        # We could potentially create dic with key as list of 26 alphabet character 

        dic = defaultdict(list)

        for word in strs:
            ch = [0] * 26
            for c in word:
                ch[ord(c) - ord('a')] += 1
            dic[tuple(ch)].append(word)
        
        return list(dic.values())
        