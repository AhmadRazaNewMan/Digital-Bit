# Binary Search on Answer: Min Feasible/Max Capacity Patterns
## What
Binary search on answer is a technique used to find the minimum or maximum value of a parameter that satisfies a certain condition. This technique is commonly used in problems where we need to find the minimum feasible or maximum capacity of something. It involves using binary search to narrow down the search space and find the optimal solution.

## Why
The reason we use binary search on answer is to reduce the time complexity of the problem. By using binary search, we can find the optimal solution in logarithmic time, which is much faster than a linear search. This technique is particularly useful in problems where the search space is large and the condition is complex.

## How
To use binary search on answer, we need to define a search space and a condition that we want to satisfy. We then use binary search to find the middle element of the search space and check if it satisfies the condition. If it does, we repeat the process on the left half of the search space. If it doesn't, we repeat the process on the right half. We continue this process until we find the optimal solution.

## One exercise or command
Try to solve the "Capacity To Ship Packages Within D Days" problem, where you need to find the minimum capacity of a ship to transport all packages within a given number of days. The command to solve this problem would be to use binary search on the possible capacities and check if it's possible to transport all packages within the given number of days.

## Further reading
* Binary search algorithm
* Search space definition
* Condition satisfaction
* Time complexity analysis
* Example problems:
  + Capacity To Ship Packages Within D Days
  + Minimize Max Distance to Closest Person
  + Koko Eating Bananas

## Senior interview checkpoint

**Prompt:** Compare monotonic queue vs heap for sliding-window max under high-throughput constraints.

**What a senior answer should include**

- Constraints first (traffic, latency, reliability, ownership boundaries).
- Tradeoffs with at least two viable alternatives.
- Failure modes, observability signals, and rollback plan.
- A measurable success criterion after rollout.
