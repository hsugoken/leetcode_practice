#Handles Empty graphs
#Cycles in the graph (by using the hash map)
"""
The approach uses a depth-first search with a dictionary to map original nodes 
to their clones. We create a new node for each original one (copying its value),
then recursively clone all neighbors, using the dictionary to handle 
already-cloned nodes and prevent infinite loops when encountering cycles in 
the graph.
"""
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # Handle edge case: empty graph
        if not node:
            return None
        
        # Dictionary to map original nodes to their clones
        # This prevents infinite recursion and handles cycles in the graph
        old_to_new = {}
        
        def dfs(original_node):
            # If we've already cloned this node, return its clone
            if original_node in old_to_new:
                return old_to_new[original_node]
            
            # Create a new copy of the current node
            clone = Node(original_node.val)
            
            # Add the mapping before processing neighbors to handle cycles
            old_to_new[original_node] = clone
            
            # Recursively clone all neighbors and connect them to our clone
            for neighbor in original_node.neighbors:
                clone.neighbors.append(dfs(neighbor))
                
            return clone
        
        # Start DFS from the given node
        return dfs(node)