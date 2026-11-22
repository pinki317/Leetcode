
class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        st=[]
        for a in asteroids:
            while st and a<0 and st[-1]>0 and st[-1]< -a:
                st.pop()
            if st and  a<0 and st[-1]>0:
                if st[-1]== -a:
                    st.pop()
            else:
                st.append(a)
        return st
