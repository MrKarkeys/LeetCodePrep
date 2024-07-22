class Solution:
    def minWindow(self, s: str, t: str) -> str:
        smap = {}
        tmap = {}
        if t =="":
            return ""
        for i in range(len(t)):
            tmap[t[i]] = 1 + tmap.get(t[i], 0)
        l = 0
        have = 0
        need = len(tmap)
        res = [0, float("infinity")]
        print(res)
        for r in range(len(s)):
            if tmap.get(s[r], 0) > 0:
                smap[s[r]] = 1 + smap.get(s[r], 0)
                if smap[s[r]] == tmap[s[r]]:
                    have += 1
            while(have == need):
                if(res[1]-res[0] > r-l):
                    res[0] = l
                    res[1] = r
                if tmap.get(s[l], 0) > 0 :
                    smap[s[l]] -= 1
                    if smap[s[l]] < tmap[s[l]]:
                        have -= 1
                l += 1
        if(res[1] > len(s)):
            return ""
        return s[res[0]:(res[1]+1)]
