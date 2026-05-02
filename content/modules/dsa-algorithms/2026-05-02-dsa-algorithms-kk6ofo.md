# Topological Sort Variants
## What
Topological sort is a linear ordering of vertices in a directed acyclic graph (DAG) such that for every directed edge `u -> v`, vertex `u` comes before `v` in the ordering. It's a fundamental concept in graph theory and has numerous applications in computer science, including course scheduling, job scheduling, and data processing.

## Why
The topological sort is essential in many real-world scenarios where the order of operations matters. For instance, in a course scheduling system, a topological sort can be used to determine the order in which courses should be taken, ensuring that prerequisites are met before advancing to more advanced courses. Similarly, in a job scheduling system, a topological sort can be used to order tasks based on their dependencies.

## How
There are two common variants of topological sort: Kahn's algorithm and the DFS-based approach. 
- Kahn's algorithm works by selecting vertices with no incoming edges and removing them from the graph, repeating the process until all vertices have been removed.
- The DFS-based approach works by performing a depth-first search on the graph and adding vertices to the ordering as they finish being visited.

## One exercise or command
To practice implementing topological sort, try writing a program that takes a DAG as input and outputs a valid topological ordering using both Kahn's algorithm and the DFS-based approach.

## Further reading
* Study the trade-offs between Kahn's algorithm and the DFS-based approach in terms of time and space complexity.
* Explore applications of topological sort in real-world scenarios, such as data processing pipelines or software build systems.
* Learn about the relationship between topological sort and other graph algorithms, such as strongly connected component decomposition.
