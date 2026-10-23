class Solution:
    def isValid(self, s: str) -> bool:
        bc = []
        for i in s:
            if i in '}])':
                if not bc:
                    return False
                last = bc.pop()
                if (i == '}' and last !='{') or (i == ']' and last !='[') or (i == ')' and last != '('):
                    return False
            else:
                bc.append(i)
        if bc:
            return False
        return True
            
        