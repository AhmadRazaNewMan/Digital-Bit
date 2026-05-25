# Binary Search on Answer Patterns
## What
Binary search on answer patterns is a technique used to solve problems where we need to find the minimum feasible or maximum capacity that satisfies certain conditions. This approach involves using binary search to find the optimal answer by iteratively narrowing down the search space.

## Why
The reason we use binary search on answer patterns is to reduce the time complexity of solving problems from O(n) to O(log n), where n is the size of the search space. This is particularly useful when dealing with large inputs or complex conditions.

## How
To apply binary search on answer patterns, we follow these steps:
- Define the search space and the conditions that the answer must satisfy.
- Initialize the low and high bounds of the search space.
- Calculate the mid value of the search space and check if it satisfies the conditions.
- If the mid value satisfies the conditions, update the high bound to mid - 1 to search for a smaller answer.
- If the mid value does not satisfy the conditions, update the low bound to mid + 1 to search for a larger answer.
- Repeat the process until the low and high bounds converge to the optimal answer.

## One exercise or command
Try solving the "Capacity To Ship Packages Within D Days" problem on LeetCode, where you need to find the minimum capacity of a ship to deliver all packages within a given number of days.

## Further reading
* Learn about the "Aggressive Cows" problem on GeeksforGeeks to practice binary search on answer patterns.
* Watch a video on YouTube explaining the concept of binary search on answer patterns and its applications.
* Read the "Binary Search" chapter in the "Introduction to Algorithms" book by Thomas H. Cormen to gain a deeper understanding of the technique.
* Practice solving problems on platforms like LeetCode, HackerRank, or CodeForces that involve binary search on answer patterns.

## Senior interview checkpoint

**Prompt:** Compare monotonic queue vs heap for sliding-window max under high-throughput constraints.

**What a senior answer should include**

- Constraints first (traffic, latency, reliability, ownership boundaries).
- Tradeoffs with at least two viable alternatives.
- Failure modes, observability signals, and rollback plan.
- A measurable success criterion after rollout.
