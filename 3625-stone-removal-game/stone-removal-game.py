class Solution:
    def canAliceWin(self, n: int) -> bool:
        stone=10
        alice=True
        while n>=stone:
            n-=stone
            alice=not alice
            stone-=1
        return not alice
        