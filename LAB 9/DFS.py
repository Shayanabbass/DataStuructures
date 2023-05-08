def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)

    print(start)

    for next in graph[start] - visited:
        dfs(graph, next, visited)
    return visited


graph = {'A': set(['B', 'E', 'D']),
         'B': set(['A', 'C']),
         'C': set(['F', 'B', 'E']),
         'D': set(['A','E']),
         'E': set(['C','A','F']),'F': set(['C','E'])}

dfs(graph, 'A')