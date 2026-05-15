# LCS and LIS Intuition
## What
LCS (Longest Common Subsequence) and LIS (Longest Increasing Subsequence) are two fundamental problems in the domain of dynamic programming. LCS involves finding the longest sequence common to two or more sequences, while LIS is about identifying the longest subsequence in a given sequence where each element is larger than the previous one. 

## Why
Understanding LCS and LIS is crucial because they are used in various applications such as data comparison, bioinformatics, and algorithmic problem-solving. Mastering these problems helps in developing a strong foundation in dynamic programming, a key skill for any aspiring programmer or data scientist.

## How
The DP state for LCS is typically defined as `dp[i][j]`, representing the length of the longest common subsequence between the first `i` characters of the first sequence and the first `j` characters of the second sequence. For LIS, the DP state `dp[i]` usually denotes the length of the longest increasing subsequence ending at index `i`. By filling up these DP tables, one can derive the lengths of the desired subsequences and even reconstruct them.

## One exercise or command
Try to define the base cases and the recurrence relations for both LCS and LIS problems to solidify your understanding of their DP states.

## Further reading
* Review the formal definitions and examples of LCS and LIS
* Explore how to reconstruct the actual subsequences from the filled DP tables
* Look into variations of these problems, such as finding the shortest common supersequence
* Apply LCS and LIS to real-world problems or coding challenges to practice your skills

## Senior interview checkpoint

**Prompt:** Compare monotonic queue vs heap for sliding-window max under high-throughput constraints.

**What a senior answer should include**

- Constraints first (traffic, latency, reliability, ownership boundaries).
- Tradeoffs with at least two viable alternatives.
- Failure modes, observability signals, and rollback plan.
- A measurable success criterion after rollout.
