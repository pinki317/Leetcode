
class StockSpanner:

    def __init__(self):
        self.st = []
        self.index = 0

    def next(self, price: int) -> int:
        while self.st and self.st[-1][0] <= price:
            self.st.pop()

        if not self.st:
            span = self.index + 1
        else:
            span = self.index - self.st[-1][1]

        self.st.append((price, self.index))
        self.index += 1

        return span
