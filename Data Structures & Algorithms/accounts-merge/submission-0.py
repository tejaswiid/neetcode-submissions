class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [1] * n

    def find(self, x):
        while x != self.par[x]:
            self.par[x] = self.par[self.par[x]]
            x = self.par[x]
        return x

    def union(self, x1, x2):
        p1, p2 = self.find(x1), self.find(x2)
        if p1 == p2:
            return False
        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
            self.rank[p1] += self.rank[p2]
        else:
            self.par[p1] = p2
            self.rank[p2] += self.rank[p1]
        return True
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:

        uf = UnionFind(len(accounts))
        emailtoindx = {}
        for i,acc in enumerate(accounts):
            for email in acc[1:]:
                if email in emailtoindx:
                    uf.union(emailtoindx[email],i)
                else:
                    emailtoindx[email] = i
        emaillist = defaultdict(list)
        for mail,ind in emailtoindx.items():
            led = uf.find(ind)
            emaillist[led].append(mail)
        res = []
        for i,e in emaillist.items():
            name = accounts[i][0]
            res.append([name]+sorted(emaillist[i]))
        return res
 
        