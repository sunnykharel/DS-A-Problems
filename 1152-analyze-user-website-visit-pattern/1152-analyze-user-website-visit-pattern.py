class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        from collections import defaultdict
        user_name_to_entries = defaultdict(list)
        
        combination_counts = defaultdict(int)
        def combinations_to_counts(combinations, combination_counts):
            encountered = set()
            n = len(combinations)
            combinations.sort(key=lambda entry: entry[1])
            for i in range(0,n-2):
                for j in range(i+1, n-1):
                    for k in range(j+1, n):
                        fst = combinations[i][0]
                        snd = combinations[j][0]
                        thrd = combinations[k][0]
                        if (fst, snd, thrd) not in encountered:
                            encountered.add((fst, snd, thrd))
                            combination_counts[(fst, snd, thrd)] +=1

        for u, t, w in zip(username, timestamp, website):
            user_name_to_entries[u].append((w, t))

        for u, combinations in user_name_to_entries.items():
            combinations_to_counts(combinations, combination_counts)
        
        max_item = None
        for item in combination_counts.items():
            if max_item == None:
                max_item = item
            else:
                if item[1] > max_item[1]:
                    max_item = item
                elif item[1] == max_item[1]:
                    if item[0] < max_item[0]:
                        max_item = item
        
        max_seq = max_item[0]
        return list(max_seq)
            
        
        
        
        
        