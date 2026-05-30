# Greedy Exchange Argument: Proving Correctness
## What
The greedy exchange argument is a method used to prove the correctness of greedy algorithms. It works by showing that any optimal solution can be transformed into the solution produced by the greedy algorithm, through a series of exchanges, without increasing the cost.

## Why
The greedy exchange argument is useful because it provides a simple and intuitive way to prove the correctness of greedy algorithms. It is often easier to apply than other methods, such as induction or contradiction, and can be used to prove the correctness of a wide range of algorithms.

## How
To apply the greedy exchange argument, we need to show that any optimal solution can be transformed into the solution produced by the greedy algorithm, through a series of exchanges, without increasing the cost. This is typically done by identifying a set of "exchange operations" that can be applied to the optimal solution, and showing that each exchange operation does not increase the cost.

## One exercise or command
Prove the correctness of the activity selection problem using the greedy exchange argument. The activity selection problem is a classic problem in computer science, where we are given a set of activities, each with a start and end time, and we need to select the maximum number of activities that do not conflict with each other.

## Further reading
* The greedy exchange argument is a key concept in the book "Introduction to Algorithms" by Thomas H. Cormen
* The activity selection problem is a classic problem in computer science, and is often used to illustrate the greedy exchange argument
* Other algorithms that can be proved correct using the greedy exchange argument include Huffman coding and the fractional knapsack problem
* The greedy exchange argument is closely related to other methods for proving correctness, such as induction and contradiction, and can often be used in combination with these methods to prove the correctness of complex algorithms.

## Senior interview checkpoint

**Prompt:** Design an approach for top-K frequent items in a streaming system with memory limits.

**What a senior answer should include**

- Constraints first (traffic, latency, reliability, ownership boundaries).
- Tradeoffs with at least two viable alternatives.
- Failure modes, observability signals, and rollback plan.
- A measurable success criterion after rollout.
