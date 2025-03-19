class Solution:
    def isNumber(self, s: str) -> bool:
        # integer followed by exponent (optional)
        # decimal can have an exponent
        # 2e(integer)
        #2.1e
        if not s:
            return False
        num_seen = False
        decimal_seen = False
        i = 0
        if s[i] in ["+", "-"]:
            i += 1
        while i<len(s):
            if s[i].isalpha():
                if s[i] not in ['e', 'E']:
                    return False
                return num_seen and self.is_integer(s[i+1:])
            elif s[i] in ["+", "-"]:
                return False
            elif s[i] == ".":
                if decimal_seen:
                    return False
                decimal_seen = True
            else:
                num_seen = True
            
            i += 1
        if num_seen:
            return True
        else:
            return False
    
    def is_integer(self, st):
        if not st:
            return False
        num_seen = False
        i = 0
        if st[i] in ["+", "-"]:
            i+=1
        while i<len(st):
            if not st[i].isdigit():
                return False
            i+=1
            num_seen = True
        if num_seen:
            return True
        else:
            return False

#TC: O(N)
#SC: O(1)