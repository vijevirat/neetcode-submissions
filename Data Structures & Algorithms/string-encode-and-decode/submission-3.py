class Solution:        

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return 'EMPTY'
        en_list=[]
        for s in strs:
            en = [str(ord(i)) for i in s]
            en_list.append(':'.join(en))
        return '::'.join(en_list)
        

    def decode(self, s: str) -> List[str]:
        dc_list = []
        if (s == 'EMPTY'):
            return []
        en_list = list(s.split("::"))
        for en in en_list:
            if len(en) == 0:
                dc_list.append("")
                continue
            dc = [chr(int(i)) for i in list(en.split(':'))]
            dc_list.append(''.join(dc))
        return dc_list
        


