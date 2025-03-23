"""
name = accounts[i][0]
email = account[i][1:]
If common email then same account
Accounts can have same name
return [{name}+ {email_sorted_order}]

Joe: em1 - em2 
Joe: em3 - em1

Joe: jm1-jm2

Pete: p1
  
"""
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        graph = collections.defaultdict(set)
        email_to_name = {} #{em1:joe, em2:joe, em3:joe, jm1:joe, jm2:joe, p1:pete}
        
        for acc in accounts:
            name = acc[0] #joe
            first_email = acc[1] #em1
            for email in acc[1:]:
                graph[email].add(first_email) 
                graph[first_email].add(email)

                email_to_name[email] = name
        #graph
        #{em1:{em2,em3}, em2:{em1},em3:{em1}, jm1:{jm2}, jm2:{jm1},p1:{p1}}
        #                                      ^
        visit = set()#{em1, em2, em3}
        res = [] 

        for email in graph:
            if email not in visit:
                #dfs returns sorted connected emails
                connected_email = self.dfs(email, graph, visit) 
                #[[joe, em1,em2, em3], [joe, jm1, jm2], [pete, p1]]
                res.append([email_to_name[email]]+connected_email)
        return res

    def dfs(self, email, graph, visit):
        #
        stack = [email] #em2, em3
        visit.add(email)
        res = []
        while stack:
            node = stack.pop()
            res.append(node) #[em1,em2, em3]
            for nei in graph[node]:
                if nei not in visit:
                    visit.add(nei)
                    stack.append(nei)
        res.sort()     
        return res
