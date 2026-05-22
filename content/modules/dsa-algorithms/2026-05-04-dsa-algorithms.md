# Shortest Path with Constraints using 0–1 BFS
## What
The 0–1 BFS algorithm is a variation of the traditional Breadth-First Search (BFS) algorithm used to find the shortest path in a graph with edge weights of 0 or 1. This concept can be extended to solve problems with constraints such as finding the shortest path in a weighted graph where edge weights are either 0 or 1, or in a graph with specific constraints like edge capacities.

## Why
The 0–1 BFS is particularly useful when dealing with graphs that have constraints, as it allows for efficient exploration of the graph while considering the constraints. This algorithm is especially useful in scenarios where the graph has a mix of edges with 0 weight (representing no cost or no distance) and edges with 1 weight (representing a unit cost or distance), and the goal is to find the shortest path that adheres to certain constraints.

## How
To implement the 0–1 BFS for finding the shortest path with constraints, we use a deque (double-ended queue) data structure. We start by pushing the source node into the deque. Then, we enter a loop that continues until the deque is empty. Inside the loop, we pop a node from the front of the deque and explore its neighbors. If the neighbor has not been visited before and the edge to the neighbor satisfies the given constraints, we mark the neighbor as visited and push it into the deque. We continue this process until we reach the destination node or the deque becomes empty. The path that leads to the destination node with the minimum number of steps (considering the constraints) is our shortest path.

## One exercise or command
Given a graph with nodes {A, B, C, D, E} and edges [(A, B, 0), (A, C, 1), (B, D, 0), (C, D, 1), (D, E, 0)], where the third element in each tuple represents the edge weight, find the shortest path from A to E using 0–1 BFS, considering the constraint that we can only traverse edges with weight 0 or 1.

## Further reading
* Review of Breadth-First Search (BFS) algorithm
* Understanding the deque data structure and its applications
* Examples of constrained shortest path problems and their solutions using 0–1 BFS
* Comparison of 0–1 BFS with other algorithms for constrained shortest path problems, such as Bellman-Ford or A\* algorithms.

## Senior interview checkpoint

**Prompt:** Compare monotonic queue vs heap for sliding-window max under high-throughput constraints.

**What a senior answer should include**

- Constraints first (traffic, latency, reliability, ownership boundaries).
- Tradeoffs with at least two viable alternatives.
- Failure modes, observability signals, and rollback plan.
- A measurable success criterion after rollout.
