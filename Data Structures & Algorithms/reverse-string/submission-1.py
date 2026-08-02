class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def revers(l,r):
            if l<r:
                revers(l+1,r-1)
                s[l],s[r] = s[r],s[l]


        revers(0,len(s)-1)