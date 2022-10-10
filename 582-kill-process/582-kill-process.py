class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        '''
        kill all pids in a subtree
        
        1. construct a tree
        
        pid =  [1, 3, 10, 5]
        ppid = [3, 0, 5, 3]
        
                0
               /      5
              3
             / \
            1  5
                \
                10
        2. dfs through the tree, kill all children of kill
        '''      
        
        tree = collections.defaultdict(list)
        for parent, child in zip(ppid, pid):
            tree[parent].append(child)
            
        kill_pids = []
        def dfs(node):
            nonlocal kill_pids
            kill_pids.append(node)
            if node in tree:
                for child in tree[node]:
                    dfs(child)
                    
        dfs(kill)
        return kill_pids
            
            
            
            
            
            
            