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
