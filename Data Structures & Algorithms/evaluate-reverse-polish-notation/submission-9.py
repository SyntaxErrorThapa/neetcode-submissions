import operator as o

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        bucket = []
        operators = {
            '+': o.add, 
            '-': o.sub, 
            '*': o.mul, 
            '/': o.truediv
        }

        for i in tokens:
            if i in operators:
                second_val = bucket.pop()
                first_val = bucket.pop()
                result = int(operators[i](int(first_val), int(second_val)))
                bucket.append(str(result))
            else:
                bucket.append(i)

        return int(bucket[0])