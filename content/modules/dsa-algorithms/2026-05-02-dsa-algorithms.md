# BFS vs DFS for Grids and Implicit Graphs
## What
Breadth-First Search (BFS) and Depth-First Search (DFS) are two fundamental graph traversal algorithms used to search and explore nodes in a graph or grid. BFS explores all the nodes at a given depth level before moving on to the next level, while DFS explores as far as possible along each branch before backtracking.

## Why
The choice between BFS and DFS depends on the problem and the structure of the grid or graph. BFS is suitable for finding the shortest path in an unweighted graph, while DFS is more suitable for searching in a graph with a complex structure or for finding a path between two nodes in a weighted graph.

## How
To implement BFS and DFS for grids and implicit graphs:
- BFS: use a queue to keep track of nodes to visit, and explore all neighbors of a node before moving on to the next level.
- DFS: use a stack to keep track of nodes to visit, and explore as far as possible along each branch before backtracking.

## One exercise or command
Try to implement BFS and DFS to find a path in a maze represented as a grid, where 0 represents an empty cell and 1 represents a wall. Start from the top-left corner and find a path to the bottom-right corner.

## Further reading
* Graph traversal algorithms and their applications
* Difference between explicit and implicit graphs
* Using BFS and DFS to solve problems in computer vision and game development
* Optimizing BFS and DFS for large-scale graphs and grids
