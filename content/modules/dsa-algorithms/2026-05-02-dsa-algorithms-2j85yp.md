# Dijkstra's Algorithm
## What
Dijkstra's algorithm is a well-known algorithm in graph theory, used for finding the shortest path between nodes in a graph. It works by iteratively exploring the graph, starting from a given source node, and maintaining a record of the shortest distance from the source to each node.

## Why
The algorithm is useful in various applications, such as network routing, traffic optimization, and resource allocation. It is particularly effective in graphs with non-negative edge weights, where the shortest path is guaranteed to be the minimum-weight path.

## How
The algorithm works by maintaining a priority queue of nodes, where the priority of each node is its current shortest distance from the source. The node with the minimum priority is extracted from the queue, and its neighbors are updated with the new shortest distances. This process is repeated until all nodes have been processed.

## One exercise or command
To implement Dijkstra's algorithm, you can use the following command in Python: `import heapq; def dijkstra(graph, source): ...`, where `graph` is a dictionary representing the graph, and `source` is the starting node.

## Further reading
* The original paper by Edsger W. Dijkstra: "A Note on Two Problems in Connexion with Graphs"
* GeeksforGeeks: "Dijkstra's algorithm"
* Wikipedia: "Dijkstra's algorithm"
* MIT OpenCourseWare: "Dijkstra's Algorithm" lecture notes
* Python implementation of Dijkstra's algorithm on GitHub
