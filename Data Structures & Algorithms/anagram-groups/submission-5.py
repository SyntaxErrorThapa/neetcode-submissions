class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for i, word in enumerate(strs):
            word = sorted(word)
            word = ''.join(word)
            if word not in dic:
                dic[word] = [i]
            else:
                dic[word].append(i)
        print(dic)
        result = []
        for key, value in dic.items():
            inside_list = []
            for v in value:
                inside_list.append(strs[v])
            result.append(inside_list)
        return result