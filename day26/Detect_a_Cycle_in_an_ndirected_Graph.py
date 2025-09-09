def has_cycle(V, edges):
    graph = {i: [] for i in range(V)}
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    visited = [False] * V
    def dfs(node, parent):
        visited[node] = True
        for neighbor in graph[node]:
            if not visited[neighbor]:
                if dfs(neighbor, node):
                    return True
            elif neighbor != parent:
                return True
        return False
    for i in range(V):
        if not visited[i]:
            if dfs(i, -1):
                return True
    return False
V = 5
edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 0]]
print(has_cycle(V, edges))
