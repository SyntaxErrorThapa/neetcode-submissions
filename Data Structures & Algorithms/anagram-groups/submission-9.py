class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Are we allowed to use sort function
        # Move through the list and sort
        # Once we sort, we have identical words
        # Then we can use dictionary to seperated different words
        dic = {}

        for word in strs:
            sorted_word = sorted(word)
            sorted_string = ''.join(sorted_word)

            if sorted_string in dic:
                dic[sorted_string].append(word)
            else:
                dic[sorted_string] = [word]
        
        new_list = [value for key, value in dic.items()]

        return new_list