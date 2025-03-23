class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        #get name from each account and map all emails with that name
        graph = collections.defaultdict(set)
        email_to_name ={}
        for account in accounts:
            name = account[0]
            first_email = account[1]
            for email in account[1:]:
                graph[email].add(first_email)
                graph[first_email].add(email)

                email_to_name[email] = name
        
        visit = set()
        res = []
        for em in graph:
            if em not in visit:
                connected_email = self.dfs(em, graph, visit)
                res.append([email_to_name[em]]+connected_email)
        return res

    def dfs(self, mail, graph, visit):
        stack = [mail]
        visit.add(mail)
        result = [] 
        while stack:
            node = stack.pop()
            result.append(node)
            for nei in graph[node]:
                if nei not in visit:
                    visit.add(nei)
                    stack.append(nei)
        result.sort()
        return result
