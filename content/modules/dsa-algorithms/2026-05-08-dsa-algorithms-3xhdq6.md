# Binary Search on Answer: Min Feasible / Max Capacity Patterns
## What
Binary search on answer is a problem-solving strategy used in algorithms where the goal is to find the minimum feasible or maximum capacity that satisfies certain conditions. This approach involves using binary search to iteratively narrow down the search space until the optimal solution is found.

## Why
This technique is useful when the problem has the following properties: the search space is large, the conditions are monotonic (i.e., if a certain value satisfies the condition, all larger or smaller values also satisfy it), and the condition can be checked efficiently. By using binary search, we can reduce the time complexity of the algorithm from linear to logarithmic.

## How
To apply binary search on answer, we need to define the search space, the condition to check, and the update rules for the search boundaries. The search space is typically defined by a range of values, and the condition is a predicate that checks whether a given value satisfies the required properties. We then use binary search to iteratively divide the search space in half and update the boundaries based on the condition check.

## One Exercise or Command
Given a positive integer `n`, find the minimum number `x` such that `x` is greater than or equal to the square root of `n`. This can be solved using binary search on answer by defining the search space as `[1, n]`, the condition as `x * x >= n`, and updating the search boundaries based on the condition check.

## Further Reading
* Key properties of binary search on answer: 
  * Monotonicity of the condition
  * Efficiency of the condition check
  * Definition of the search space and update rules
* Example problems: 
  * Finding the minimum number of steps to reach a target value
  * Determining the maximum capacity of a system
  * Searching for the minimum or maximum value that satisfies a given condition
* Related techniques: 
  * Linear search
  * Exponential search
  * Ternary search
