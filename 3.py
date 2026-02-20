"""3. The "Dynamic Network Vulnerability" (Tarjan's/Graphs)
○ Problem: Given a communication network represented as an undirected graph,
identify all "Critical Links" (Bridges). A link is critical if its removal disconnects the
network.
○ Complexity Requirement: Solve in O(V + E) using a single DFS pass.
"""

def find_bridges(graph):
    time = 0
    visited = set()
    disc = {}
    low = {}
    parent = {}
    bridges = []

    def dfs(u):
        nonlocal time
        visited.add(u)
        disc[u] = low[u] = time
        time += 1

        for v in graph[u]:
            if v not in visited:
                parent[v] = u
                dfs(v)
                low[u] = min(low[u], low[v])

                if low[v] > disc[u]:
                    bridges.append((u, v))
            elif parent.get(u) != v:
                low[u] = min(low[u], disc[v])

    for node in graph:
        if node not in visited:
            dfs(node)

    return bridges

if __name__ == "__main__":
    graph = {
        0: [1, 2],
        1: [0, 2],
        2: [0, 1, 3],
        3: [2]
    }

    print(find_bridges(graph))