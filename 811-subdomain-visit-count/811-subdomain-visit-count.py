class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        maps = collections.defaultdict(int)
        '''
        go through each split string once
        with the count
        '''
        
        def join_function(tup):
            return '{} {}'.format(tup[1], tup[0])
            
        
        
        for domain in cpdomains:
            split = domain.split()
            count, subdomains = int(split[0]), split[1]
            subdomainbuilder = ''
            for subdomain in reversed(subdomains.split('.')):
                if subdomainbuilder != '':
                    subdomainbuilder = '.'+subdomainbuilder
                subdomainbuilder = subdomain+subdomainbuilder
                maps[subdomainbuilder]+=count
                
        return [join_function(tup) for tup in maps.items()]
                
        