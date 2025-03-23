class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # This is a cycle detection problem in a directed graph
        # If there is a cycle in the graph, all courses cannot be completed
        # We use topological sort with BFS to detect if all courses can be finished
        
        # Step 1: Build graph representation
        # (a) Create adjacency list mapping prerequisite to course
        # (b) Calculate the indegree (number of prerequisites) for each course
        adj = collections.defaultdict(set)
        indegree = [0] * numCourses

        for prereq in prerequisites:
            cur_course = prereq[0]
            req_course = prereq[1]
            # Edge direction: req_course -> cur_course (prerequisite leads to course)
            adj[req_course].add(cur_course)
            indegree[cur_course] += 1
        
        # Step 2: Find courses with 0 indegree (no prerequisites)
        # These are our starting points for BFS
        # Example: In A->B->C and D->B, courses A and D have 0 indegree
        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        
        # Step 3: Perform BFS traversal
        visited = set()
        while queue:
            node = queue.popleft()
            visited.add(node)
            
            # Process all neighbors (courses that depend on current course)
            for nei in adj[node]:
                # Decrease indegree as we've completed one of its prerequisites
                indegree[nei] -= 1
                # If all prerequisites are met, add to queue
                if indegree[nei] == 0:
                    queue.append(nei)
        
        # If there's a cycle, nodes in the cycle will never have indegree=0
        # So they won't be processed and visited.size < numCourses
        return len(visited) == numCourses