class Solution:
    def calculate(self, s: str) -> int:
        n=len(s)
        st=[]
        num=0
        res=0
        sign=1
        for i in range(0,n):
            if s[i]== ' ':
                continue
            if s[i].isdigit():
                num=num*10+int(s[i])
            elif s[i]=='+':
                res+=num*sign
                num=0
                sign=1
            elif s[i]=='-':
                res+=num*sign
                num=0
                sign=-1
            elif s[i]=='(':
                st.append(res)
                st.append(sign)
                res=0
                num=0
                sign=1
            elif s[i]==')':
                res+=num*sign
                num=0
                st_sign=st[-1]
                st.pop()
                last_res=st[-1]
                st.pop()
                res*=st_sign
                res+=last_res
        res+=num*sign
        return res



        
        