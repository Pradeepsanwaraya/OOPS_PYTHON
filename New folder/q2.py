class Solution(object):
    def findDifference(self, nums1, nums2):
        a=[]
        b=[]

        for i in nums1:
            if i not in nums2 and i not in a:
                a.append(i)

        for i in nums2:
            if i not in nums1 and i not in b:
                b.append(i)

        return [a,b]