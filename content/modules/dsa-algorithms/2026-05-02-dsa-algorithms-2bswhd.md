# Two Pointers on Sorted Arrays and Duplicates
## What
Two pointers is a technique used in array or string problems, where two pointers are initialized at different positions in the array and moved based on certain conditions. When dealing with sorted arrays and duplicates, this technique can be particularly useful for finding or removing duplicates.

## Why
The two pointers technique is efficient for solving problems involving sorted arrays and duplicates because it allows us to traverse the array in a single pass, reducing the time complexity to O(n), where n is the number of elements in the array. This is especially important when dealing with large datasets.

## How
To apply the two pointers technique to a sorted array with duplicates, we typically initialize two pointers, one at the beginning of the array and one at the second element. We then compare the elements at these positions and move the pointers accordingly. For example, if we want to remove duplicates from a sorted array, we can move the first pointer forward when we encounter a duplicate, and move the second pointer forward when we encounter a new element.

## One exercise or command
Remove duplicates from a sorted array [1, 1, 2, 3, 3, 3, 4, 5, 5] using the two pointers technique.

## Further reading
* The two pointers technique can be used in a variety of problems, including:
  * Finding the first pair of elements in a sorted array that add up to a given sum
  * Removing duplicates from a sorted array
  * Finding the maximum sum of a subarray within a given size
  * Merging two sorted arrays into a single sorted array
  * Implementing binary search in a sorted array
* The two pointers technique can be applied to other data structures, such as linked lists and strings
* The time complexity of the two pointers technique can vary depending on the specific problem, but it is often O(n) or O(log n)

## Senior interview checkpoint

**Prompt:** Compare monotonic queue vs heap for sliding-window max under high-throughput constraints.

**What a senior answer should include**

- Constraints first (traffic, latency, reliability, ownership boundaries).
- Tradeoffs with at least two viable alternatives.
- Failure modes, observability signals, and rollback plan.
- A measurable success criterion after rollout.
