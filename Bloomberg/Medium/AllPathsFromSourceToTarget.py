
#DFS

class Solution:
    def allPathsSourceTarget(self, graph):
        # Start from root (node 0) 
        # Find every path we can take
        # go through each path to see the path we are building to get to the final node.
        
        end = len(graph) - 1
        
        def dfs(node, path, output):
            if node == end:
                output.append(path)
                
            # for each next node in our graph
            for nx in graph[node]:
                dfs(nx, path + [nx],output)
                # Build path and add next (nx)
                
        output = []
        dfs(0, [0], output)
        return output