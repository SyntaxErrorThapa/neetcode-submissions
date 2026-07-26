class Solution:

    def encode(self, strs: List[str]) -> str:
        send = ""
        for word in strs:
            send += f"{len(word)}#{word}" 
        print(send)
        return send

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        while i < len(s):
            # Find the delimiter to get the full length number
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1  # Skip past '#'
            result.append(s[i:i+length])
            i += length

        return result




        

