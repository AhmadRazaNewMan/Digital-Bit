# Greedy Exchange Argument: Proving Correctness
## What
The greedy exchange argument is a technique used to prove the correctness of greedy algorithms. It involves showing that any optimal solution can be transformed into the solution produced by the greedy algorithm, by exchanging elements one at a time, without decreasing the quality of the solution.

## Why
The greedy exchange argument is useful because it provides a way to prove the correctness of greedy algorithms without having to examine all possible solutions. This can be particularly useful for problems where the number of possible solutions is very large.

## How
To use the greedy exchange argument, we start with an optimal solution and show that we can transform it into the solution produced by the greedy algorithm, by exchanging elements one at a time. We must show that each exchange does not decrease the quality of the solution, and that the final solution produced is the same as the one produced by the greedy algorithm.

## One exercise or command
Try to prove the correctness of the activity selection problem using the greedy exchange argument. The activity selection problem is to select the maximum number of activities that can be performed by a single person, given a set of activities and their start and end times.

## Further reading
* The greedy exchange argument is a key component of the proof of correctness for many greedy algorithms, including Huffman coding and the activity selection problem.
* For more information on the greedy exchange argument, see:
  + "Introduction to Algorithms" by Thomas H. Cormen
  + "Algorithms" by Robert Sedgewick and Kevin Wayne
  + "The Design of Approximation Algorithms" by David P. Williamson and David B. Shmoys

## Senior interview checkpoint

**Prompt:** Design an approach for top-K frequent items in a streaming system with memory limits.

**What a senior answer should include**

- Constraints first (traffic, latency, reliability, ownership boundaries).
- Tradeoffs with at least two viable alternatives.
- Failure modes, observability signals, and rollback plan.
- A measurable success criterion after rollout.
