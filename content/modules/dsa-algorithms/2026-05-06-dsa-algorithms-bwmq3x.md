# Union-Find with Path Compression
## What
Union-find, also known as disjoint-set, is a data structure that stores a collection of disjoint sets. It supports two main operations: `find(a)` which returns the representative (or the "parent") of the set that `a` belongs to, and `union(a, b)` which merges the sets that `a` and `b` belong to.

## Why
The union-find data structure with path compression is particularly useful in scenarios where we need to efficiently manage a large number of elements that are grouped into sets, such as in network connectivity analysis, social network analysis, or database query optimization. Path compression is an optimization technique that reduces the time complexity of the `find` operation by flattening the tree structure of the sets.

## How
The union-find data structure with path compression works as follows:
- Each element is initially in its own set.
- When `find(a)` is called, the algorithm traverses the tree from `a` to the root, and then compresses the path by making all nodes point directly to the root.
- When `union(a, b)` is called, the algorithm finds the roots of the sets that `a` and `b` belong to, and then merges the two sets by making one root point to the other.

## One exercise or command
Try implementing the union-find data structure with path compression in your favorite programming language, and use it to solve the following problem: given a list of `n` elements and a list of `m` pairs of elements that are connected, find the number of connected components in the graph.

## Further reading
* The union-find data structure is also known as the disjoint-set data structure, and is often used in Kruskal's algorithm for finding the minimum spanning tree of a graph.
* Path compression is just one of several optimization techniques that can be used to improve the performance of the union-find data structure, others include union by rank and weighted union.
* The time complexity of the union-find data structure with path compression is nearly constant time for both the `find` and `union` operations, making it very efficient for large datasets.
* The union-find data structure has many real-world applications, including network connectivity analysis, image processing, and database query optimization.

## Senior interview checkpoint

**Prompt:** Design an approach for top-K frequent items in a streaming system with memory limits.

**What a senior answer should include**

- Constraints first (traffic, latency, reliability, ownership boundaries).
- Tradeoffs with at least two viable alternatives.
- Failure modes, observability signals, and rollback plan.
- A measurable success criterion after rollout.
