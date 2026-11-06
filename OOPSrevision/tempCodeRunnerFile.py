    # def __init__(self,l):
    #     self.Lenght=l
    #     print("Lenght is ",self.Lenght)


    
class Solution(object):
    def findMinArrowShots(self, points):
        points.sort(key=lambda x: x[1])

        arrows = 1
        end = points[0][1]

        for i in range(1, len(points)):

            if points[i][0] > end:
                arrows = arrows + 1
                end = points[i][1]

        return arrows

class Solution(object):
    def findMinArrowShots(self, points):
        points.sort(key=lambda x: x[1])

        arrows = 1
        end = points[0][1]

        for i in range(1, len(points)):

            if points[i][0] > end:
                arrows = arrows + 1
                end = points[i][1]

        return arrows


class Solution(object):
    def maxScore(self, nums1, nums2, k):
        pairs = []

        for i in range(len(nums1)):
            pairs.append([nums2[i], nums1[i]])

        pairs.sort(reverse=True)

        import heapq

        heap = []
        total = 0
        ans = 0

        for i in range(len(pairs)):
            a = pairs[i][1]
            b = pairs[i][0]

            heapq.heappush(heap, a)
            total = total + a

            if len(heap) > k:
                x = heapq.heappop(heap)
                total = total - x

            if len(heap) == k:
                score = total * b

                if score > ans:
                    ans = score

        return ans

class Solution(object):
    def maxScore(self, nums1, nums2, k):
        pairs = []

        for i in range(len(nums1)):
            pairs.append([nums2[i], nums1[i]])

        pairs.sort(reverse=True)

        import heapq

        heap = []
        total = 0
        ans = 0

        for i in range(len(pairs)):
            a = pairs[i][1]
            b = pairs[i][0]

            heapq.heappush(heap, a)
            total = total + a

            if len(heap) > k:
                x = heapq.heappop(heap)
                total = total - x

            if len(heap) == k:
                score = total * b

                if score > ans:
                    ans = score

        return ans

class Solution(object):
    def maxScore(self, nums1, nums2, k):
        pairs = []

        for i in range(len(nums1)):
            pairs.append([nums2[i], nums1[i]])

        pairs.sort(reverse=True)

        import heapq

        heap = []
        total = 0
        ans = 0

        for i in range(len(pairs)):
            a = pairs[i][1]
            b = pairs[i][0]

            heapq.heappush(heap, a)
            total = total + a

            if len(heap) > k:
                x = heapq.heappop(heap)
                total = total - x

            if len(heap) == k:
                score = total * b

                if score > ans:
                    ans = score

        return ans
class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        low, high = 1, n

        while low <= high:
            mid = low + (high - low) // 2
            res = guess(mid)

            if res == 0:
                return mid
            elif res == -1:    # guess is too high, search left half
                high = mid - 1
            else:              # res == 1, guess is too low, search right half
                low = mid + 1class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        low, high = 1, n

        while low <= high:
            mid = low + (high - low) // 2
            res = guess(mid)

            if res == 0:
                return mid
            elif res == -1:    # guess is too high, search left half
                high = mid - 1
            else:              # res == 1, guess is too low, search right half
                low = mid + 1class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        low, high = 1, n

        while low <= high:
            mid = low + (high - low) // 2
            res = guess(mid)

            if res == 0:
                return mid
            elif res == -1:    # guess is too high, search left half
                high = mid - 1
            else:              # res == 1, guess is too low, search right half
                low = mid + 1class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        low, high = 1, n

        while low <= high:
            mid = low + (high - low) // 2
            res = guess(mid)

            if res == 0:
                return mid
            elif res == -1:    # guess is too high, search left half
                high = mid - 1
            else:              # res == 1, guess is too low, search right half
                low = mid + 1class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        low, high = 1, n

        while low <= high:
            mid = low + (high - low) // 2
            res = guess(mid)

            if res == 0:
                return mid
            elif res == -1:    # guess is too high, search left half
                high = mid - 1
            else:              # res == 1, guess is too low, search right half
                low = mid + 1