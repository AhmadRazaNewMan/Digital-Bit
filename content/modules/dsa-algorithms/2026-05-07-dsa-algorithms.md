# Binary Search on Answer: Min Feasible / Max Capacity Patterns
## What
Binary search on answer is a technique used to find the minimum feasible or maximum capacity solution to a problem. It involves using binary search to find the optimal answer by iteratively narrowing down the search space. This technique is commonly used in problems where the answer is a number or a value that needs to be minimized or maximized.

## Why
The reason why binary search on answer is useful is that it allows us to solve problems efficiently by reducing the search space by half at each step. This technique is particularly useful when the problem has a large search space and we need to find the optimal solution quickly.

## How
To apply binary search on answer, we need to define a function that checks if a given answer is feasible or not. We then use binary search to find the minimum or maximum feasible answer. The steps involved are:
* Define the search space (min and max possible answers)
* Define a function to check if a given answer is feasible
* Use binary search to find the minimum or maximum feasible answer

## One exercise or command
Try to solve the "Capacity To Ship Packages Within D Days" problem on LeetCode, where you need to find the minimum capacity of a ship to deliver all packages within a given number of days. The command to solve this problem using binary search on answer is: `def shipWithinDays(weights, days): ...` 

## Further reading
* Key characteristics of binary search on answer:
  + Minimax problems
  + Feasibility checks
  + Large search spaces
* Common problem patterns:
  + Scheduling problems
  + Resource allocation problems
  + Optimization problems
* Practice problems:
  + LeetCode: "Capacity To Ship Packages Within D Days"
  + LeetCode: "Koko Eating Bananas"

## Senior interview checkpoint

**Prompt:** Design an approach for top-K frequent items in a streaming system with memory limits.

**What a senior answer should include**

- Constraints first (traffic, latency, reliability, ownership boundaries).
- Tradeoffs with at least two viable alternatives.
- Failure modes, observability signals, and rollback plan.
- A measurable success criterion after rollout.
