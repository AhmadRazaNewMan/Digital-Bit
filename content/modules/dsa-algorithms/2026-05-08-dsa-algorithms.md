# Longest Common Subsequence Intuition
## What
The Longest Common Subsequence (LCS) and Longest Increasing Subsequence (LIS) are two dynamic programming problems that deal with finding the longest subsequence in a given sequence or between two sequences. The LCS problem involves finding the longest sequence that appears in the same relative order in two sequences, while the LIS problem involves finding the longest subsequence in a single sequence where each element is larger than the previous one.

## Why
Understanding the intuition behind LCS and LIS is crucial for solving various dynamic programming problems. It helps in breaking down complex problems into smaller sub-problems, recognizing overlapping sub-problems, and applying dynamic programming principles to solve them efficiently.

## How
To develop the intuition for LCS and LIS, it is essential to understand the concept of DP states. In the case of LCS, the DP state `dp[i][j]` represents the length of the longest common subsequence between the first `i` characters of the first sequence and the first `j` characters of the second sequence. For LIS, the DP state `dp[i]` represents the length of the longest increasing subsequence ending at index `i`. By filling up these DP states in a bottom-up manner, we can derive the longest common subsequence or the longest increasing subsequence.

## One exercise or command
Try to find the LCS between the sequences "ABCBDAB" and "BDCABA" by filling up the DP states manually.

## Further reading
* Review the properties of dynamic programming and how it applies to LCS and LIS problems
* Practice solving LCS and LIS problems on platforms like LeetCode or GeeksforGeeks
* Explore other dynamic programming problems that involve finding the longest or shortest subsequence, such as the Shortest Common Supersequence problem
* Read about the time and space complexity of LCS and LIS algorithms and how they can be optimized for large inputs

## Senior interview checkpoint

**Prompt:** Design an approach for top-K frequent items in a streaming system with memory limits.

**What a senior answer should include**

- Constraints first (traffic, latency, reliability, ownership boundaries).
- Tradeoffs with at least two viable alternatives.
- Failure modes, observability signals, and rollback plan.
- A measurable success criterion after rollout.
