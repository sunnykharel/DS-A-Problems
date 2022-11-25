class Solution:
    def __init__(self):
        self.grid, self.n, self.m = None, None, None
        self.distance_to_ones = collections.defaultdict(dict)
        self.coord_to_valid_neighbors = None

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

    def calc_distance_to_single_coord_with_one(self, coord_with_one, bfs_number):
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
                for n in self.coord_to_valid_neighbors[node]:
                    if n not in visited and self.grid[n[0]][n[1]] == -bfs_number:
                        self.grid[n[0]][n[1]] -= 1
                        curr.append(n)
                        visited.add(n)
            prev = curr
            curr = []
            bfs_level += 1
    
    def generate_valid_neighbords(self, grid):
        valid_neighbors = collections.defaultdict(list)
        for x in range(self.n):
            for y in range(self.m):
                neighs = [(x+1, y), (x-1, y), (x, y-1), (x, y+1)]
                for neigh in neighs:
                    if self.coord_in_bounds_and_is_zero(neigh):
                        valid_neighbors[(x,y)].append(neigh)
        return valid_neighbors
                        
                

    def shortestDistance(self, grid: List[List[int]]) -> int:
        self.grid = grid
        self.n, self.m = len(grid), len(grid[0])
        coords_with_ones = self.coords_with_ones()
        
        self.coord_to_valid_neighbors = self.generate_valid_neighbords(grid)
        
        for bfs_number, coord_with_one in enumerate(coords_with_ones):
            self.calc_distance_to_single_coord_with_one(
                coord_with_one,
                bfs_number
            )

        min_distance = -1
        for zero_coord, distances in self.distance_to_ones.items():
            if grid[zero_coord[0]][zero_coord[1]] != -(bfs_number+1):
                continue
            if len(distances) != len(coords_with_ones):
                continue
            distance = sum(val for val in distances.values())
            if min_distance == -1:
                min_distance = distance
            else:
                min_distance = min(min_distance, distance)
        return min_distance
