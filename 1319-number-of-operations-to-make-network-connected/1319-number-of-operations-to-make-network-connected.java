class Solution {
    public int makeConnected(int n, int[][] connections) {
        //we want to create a tree, and remove the cycles
        //doing a bfs, we get 0, then it's two children
        //bfs gives us how many edges we actually need
        //what ever left over edges we have can be used to connect others
        
        //implementation
        /*
            we start a bfs from a node, count how many nodes it can reach
            we need to create a graph first
        
        */
        if (connections.length < n-1)
            return -1;
        
        
        Map<Integer, Set<Integer>> graph = new HashMap<>();
        
        for (int[] node: connections){
            if (!graph.containsKey(node[0])){
                graph.put(node[0], new HashSet<Integer>());
            }
            if (!graph.containsKey(node[1])){
                graph.put(node[1], new HashSet<Integer>());
            }
            graph.get(node[0]).add(node[1]);
            graph.get(node[1]).add(node[0]);
        }
        // do the bfs
        int num_forests = 0;
        num_forests += n - graph.keySet().size();
        Set<Integer> visited = new HashSet<>();

        //bfs for every node
        
        for (int start_node: graph.keySet()){
            if (visited.contains(start_node)){
                continue;
            }
            Queue<Integer> queue = new LinkedList<>();
            queue.add(start_node);
            visited.add(start_node);
            num_forests++;
            while (!queue.isEmpty()){
                int node = queue.poll();
                if (graph.containsKey(node)){
                    for (Integer child : graph.get(node)){
                        if(!visited.contains(child)){
                            queue.add(child);
                            visited.add(child);
                        }   
                    }
                }
            }
        }
        //there may be many forests, so we want to do a bfs from every node basically
        return num_forests-1;
        
        
        // return connections.length-connectionsUsed;
        // return 0;   
    }
}