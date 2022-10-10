class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        for i in range(len(points)):
            x = points[i][0]
            y = points[i][1]
            points[i] = (x, y, (x**2+y**2)**(1/2))
        points.sort(key=lambda x: x[2])
        return [(points[i][0], points[i][1]) for i in range(0, K)]
            
        