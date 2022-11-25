class Solution:
    def __init__(self):
        self.grid, self.n, self.m = None, None, None
        self.distance_to_ones = collections.defaultdict(dict)

    def coords_with_ones(self):
        coords = []
        for i in range(self.n):
            for j in range(self.m):
                if self.grid[i][j] == 1:
                    coords.append((i,j))
        return coords
    
    def coord_in_bounds_and_is_zero(self, coord):
        x, y = coord
        return 0 <= x < self.n and 0 <= y < self.m and self.grid[x][y] == 0

    def calc_distance_to_single_coord_with_one(self, coord_with_one):
        node = coord_with_one
        q = collections.deque()
        q.append(node)
        visited = { node }

        bfs_level = 0
        prev = [ node ]
        curr = []
        while len(prev) > 0:
            for node in prev:
                if node!=coord_with_one:
                    self.distance_to_ones[node][coord_with_one] = bfs_level
                x, y = node
                neighbors = [(x+1, y), (x-1, y), (x, y-1), (x, y+1)]
                for n in neighbors:
                    if self.coord_in_bounds_and_is_zero(n):
                        if n not in visited:
                            curr.append(n)
                            visited.add(n)
            prev = curr
            curr = []
            bfs_level += 1

    def shortestDistance(self, grid: List[List[int]]) -> int:
        self.grid = grid
        self.n, self.m = len(grid), len(grid[0])
        
        coords_with_ones = self.coords_with_ones()

        for coord_with_one in coords_with_ones:
            self.calc_distance_to_single_coord_with_one(coord_with_one)

        min_distance = -1
        for zero_coord, distances in self.distance_to_ones.items():
            if len(distances) != len(coords_with_ones):
                continue
            distance = sum(val for val in distances.values())
            if min_distance == -1:
                min_distance = distance
            else:
                min_distance = min(min_distance, distance)
        return min_distance
