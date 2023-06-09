# BFS algorithm in Python


import collections

# BFS algorithm
def bfs(graph, root):

    visited, queue = set(), collections.deque([root])
    visited.add(root)

    while queue:

        # Dequeue a vertex from queue
        vertex = queue.popleft()
        print(str(vertex) + " ", end="")

        # If not visited, mark it as visited, and
        # enqueue it
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)


if __name__ == '__main__':
    graph = {'A': set(['B', 'E', 'D']),
         'B': set(['A', 'C']),
         'C': set(['F', 'B', 'E']),
         'D': set(['A','E']),
         'E': set(['C','A','F']),'F': set(['C','E'])}

    print("Following is Breadth First Traversal: ")
    bfs(graph, 'A')