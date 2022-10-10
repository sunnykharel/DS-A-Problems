class Solution {
    public int minReorder(int n, int[][] connections) {
        //there is only one path to each node ... 
        //we do a bfs and flip the directions if we need to
        //we create a tree on the connections from zero
        //we add to the queue in row by row fashion
        //first find all of the zeros
        //if the zeros are on int[1] then we convert them
        
        //either 2_3 in the map or 3_2
        //if the wrong direction is in there bad
        //we want a graph listing all the possible nodes something is connected to
        int in = 1;
        int out = -1;
        Map<Integer, Map<Integer, Integer>> map = new HashMap<>();
        for (int[] connection : connections){
            if(!map.containsKey(connection[0])){
                map.put(connection[0], new HashMap<>());
            }
            if(!map.containsKey(connection[1])){
                map.put(connection[1], new HashMap<>());
            }
            map.get(connection[0]).put(connection[1], out);
            map.get(connection[1]).put(connection[0], in);
        }
        
        Set<Integer> visited = new HashSet<>();
        
        Queue<Integer> q = new LinkedList<>();
        
        q.add(0);
        int flipsNeeded = 0;
        while (!q.isEmpty()){
            Integer node = q.poll();
            visited.add(node);
            for (Integer neighbor : map.get(node).keySet()){
                if (visited.contains(neighbor)){
                    continue;
                }
                if (map.get(node).get(neighbor) == out){
                    flipsNeeded+=1;
                }
                q.add(neighbor);
            }
        }
        return flipsNeeded;
        
        
     
        
    }
}