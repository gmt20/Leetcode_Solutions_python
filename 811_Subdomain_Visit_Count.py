class Solution:
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        final = []
        from collections import defaultdict
        dic = defaultdict(int)
        for word in cpdomains:
            n, d = word.split()
            dic[d] +=int(n)
            for i in range(len(d)):
                if d[i] == '.': dic[d[i + 1:]] += int(n)
        final = [str(dic[k]) + ' ' + k for k in dic]
        return final
