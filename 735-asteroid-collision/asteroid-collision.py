
class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        arr = asteroids.copy()

        while True:
            changed = False
            i = 0

            while i < len(arr) - 1:
                if arr[i] > 0 and arr[i+1] < 0:

                    if abs(arr[i]) < abs(arr[i+1]):
                        arr.pop(i)
                    elif abs(arr[i]) > abs(arr[i+1]):
                        arr.pop(i+1)
                    else:
                        arr.pop(i)
                        arr.pop(i)

                    changed = True
                    break

                else:
                    i += 1

            if not changed:
                break

        return arr
