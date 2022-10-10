class Solution:
    def generateSentences(self, synonyms: List[List[str]], text: str) -> List[str]:
        repeated_groups_found = None
        while repeated_groups_found is True or repeated_groups_found is None:
            repeated_groups_found=False
            filtered_synonym_groups = []
            for syn in synonyms:
                syn.sort()
            synonyms.sort(key=lambda x: x[0])

            for synonym in synonyms:
                words = set(synonym)
                word1 = synonym[0]
                word2 = synonym[1]
                has_another_group = False
                for i,group in enumerate(filtered_synonym_groups):
                    words.intersection(set(group))
                    if len(words.intersection(set(group))) > 0:
                        has_another_group = True
                        filtered_synonym_groups[i] = list(set(group+synonym))
                        break
                print(synonym, has_another_group)
                if has_another_group and repeated_groups_found is None:
                    repeated_groups_found = True
                else:
                    repeated_groups_found = has_another_group or repeated_groups_found
                if not has_another_group:
                    filtered_synonym_groups.append(synonym)
            
            synonyms = filtered_synonym_groups
            print(synonyms)
        print(synonyms)
        

            
        
        
        words_to_syn_index = dict()
        for i,synonym in enumerate(synonyms):
            synonym.sort()
            for word in synonym:
                words_to_syn_index[word] = i
        
        # print(words_to_syn_index)

        sentence = text.split(' ')

        sentence_index_to_syn_index = dict()
        for i,word in enumerate(sentence):
            if word in words_to_syn_index:
                sentence_index_to_syn_index[i] = words_to_syn_index[word]
        
        # print(sentence_index_to_syn_index)

        n = len(sentence)
        output = []
        def dfs(index):

            if index == n:
                output.append(' '.join(sentence))
                return
            if index not in sentence_index_to_syn_index:
                dfs(index+1)
                return
                

            syn_index = sentence_index_to_syn_index[index]
            syn = synonyms[syn_index]

            for i in range(len(syn)):
                # print(i, syn)
                sentence[index] = syn[i]
                dfs(index+1)
            return
        

        dfs(0)
        return output