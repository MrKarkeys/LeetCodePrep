class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans = []
        for i in range(n):
            val = i+1
            if val%3==0 and val%5==0:
                ans.append("FizzBuzz")
            elif val%3==0:
                ans.append("Fizz")
            elif val%5==0:
                ans.append("Buzz")
            else:
                ans.append(str(val))
        return ans
