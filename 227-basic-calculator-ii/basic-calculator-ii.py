
class Solution:
    def calculate(self, s: str) -> int:
        nums = []
        op = []
        num = 0

        for ch in s:
            if ch == ' ':
                continue

            if ch.isdigit():
                num = num * 10 + int(ch)
            else:
                nums.append(num)
                op.append(ch)
                num = 0

        nums.append(num)

        # First solve * and /
        i = 0
        while i < len(op):
            if op[i] == '*' or op[i] == '/':
                a = nums[i]
                b = nums[i + 1]

                if op[i] == '*':
                    val = a * b
                else:
                    sign = -1 if (a < 0) != (b < 0) else 1
                    val = sign * (abs(a) // abs(b))

                nums[i] = val
                nums.pop(i + 1)
                op.pop(i)

            else:
                i += 1

        # Then solve + and -
        result = nums[0]

        for i in range(len(op)):
            if op[i] == '+':
                result += nums[i + 1]
            else:
                result -= nums[i + 1]

        return result
