class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #It should have a pre-req that cna be taken and has no loop
        #1)(a) Create adjacency list mapping pre-requisite to course
        #1)(b) Calculate the indegree of the course as well
        #2) Find out nodes with 0 indegree
        #3) Do BFS and see if visited nodes are equal to numcourses
        
        #1)
        # adj = collections.defaultdict(list)
        adj = collections.defaultdict(set)
        indegree = [0]*numCourses

        for prereq in prerequisites:
            cur_course = prereq[0]
            req_course = prereq[1]
            # adj[req_course].append(cur_course)
            adj[req_course].add(cur_course)
            indegree[cur_course] += 1
        #2)
        queue = deque()
        for i in range(numCourses):
            if indegree[i]==0:
                queue.append(i)
        #3)
        visited = set()
        while queue:
            node = queue.popleft()
            visited.add(node)
            for nei in adj[node]:
                indegree[nei] -= 1
                if indegree[nei]==0:
                    queue.append(nei)
        return len(visited)==numCourses

        
        
