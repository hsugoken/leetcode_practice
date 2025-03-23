class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #ingeneral it is a cycle detection problem. If there is a cycle in the 
        #graph of pre-req => course 
        #calculate indegree of course as well
        #Find out nodes with 0 indegree
        #Do BFS and see if visited nodes are equal to numCourses
        
        adj = collections.defaultdict(set)
        indegree = [0]*numCourses

        for prereq in prerequisites:
            cur_course = prereq[0]
            req_course = prereq[1]
            #req_course -> cur_course
            adj[req_course].add(cur_course)
            indegree[cur_course] += 1
        #Now we find nodes with 0 indegree
        #Basically the req-course that has no req_course
        #A->B->C
        #D->B
        #Here A and D are with 0 indegree
        queue = deque()
        for i in range(numCourses):
            if indegree[i]==0:
                queue.append(i)
        #Now we do BFS
        visit = set()
        while queue:
            node = queue.popleft()
            visit.add(node)
            #now visit all the neighbors
            for nei in adj[node]:
                #we decrease the indegree of nei as we have already processed
                #the current node and we moved to the nei and we have to process it
                indegree[nei] -= 1
                if indegree[nei]==0:
                    queue.append(nei)
        return len(visit)==numCourses