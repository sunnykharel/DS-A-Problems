class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # we make the tree 
        # we then look for paths from 

        tree = collections.defaultdict(list)
        for ticket in tickets:
            tree[ticket[0]].append(ticket[1])

        for _, links in tree.items():
            links.sort()
        
        def recursion(node, depth, path):
            nonlocal tree
            if len(path)==len(tickets)+1:
                return True
            elif node not in tree:
                return False
            else:
                for i,child in enumerate(tree[node]):
                    if child == '\0':
                        continue
                    tree[node][i]='\0'
                    path.append(child)
                    if recursion(child, depth+1, path):
                        tree[node][i]=child
                        return True
                    else:
                        path.pop()
                        tree[node][i] = child
                    
                return False
                        
        for i,child in enumerate(tree['JFK']):
            path = ['JFK', child]
            tree['JFK'][i] = '\0'
            if recursion(child, 1, path):
                return path
            
            else:
                tree['JFK'][i] = child
