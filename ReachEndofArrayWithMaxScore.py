class Solution:
    def convertDateToBinary(self, date: str) -> str:
        datearr = date.split("-")
        ans = ""
        for i in datearr:
            temp = str(bin(int(i)))
            ans += temp[2:len(temp)]
            ans += "-"
        return ans[0:len(ans)-1]
