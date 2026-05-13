# Rolling Hash and Rabin-Karp for Substring Search
## What
Rolling hash and Rabin-Karp are algorithms used for substring search, a common problem in computer science. The goal is to find all occurrences of a given pattern within a text. Rolling hash is a technique used to quickly calculate the hash value of a substring, while Rabin-Karp is an algorithm that utilizes rolling hash to efficiently search for substrings.

## Why
The Rabin-Karp algorithm is useful when dealing with large texts and patterns, as it reduces the number of comparisons required to find a match. It has an average time complexity of O(n+m), making it more efficient than a brute-force approach for large inputs. Additionally, rolling hash allows for fast calculation of hash values, enabling the algorithm to quickly eliminate non-matching substrings.

## How
The Rabin-Karp algorithm works by calculating the hash value of the pattern and the initial substring of the text with the same length as the pattern. It then compares these hash values and checks for a match. If the hash values match, it performs a character-by-character comparison to confirm the match. The rolling hash technique is used to calculate the hash value of the next substring by removing the leading character's contribution and adding the next character's contribution.

## One exercise or command
Try implementing the Rabin-Karp algorithm to search for the substring "abc" in the text "abcabcabc" using a rolling hash with a base of 256 and a modulus of 101.

## Further reading
* The Rabin-Karp algorithm is a variation of the Knuth-Morris-Pratt algorithm and the Boyer-Moore algorithm, which also solve the substring search problem.
* Rolling hash is used in other algorithms, such as the Karp-Rabin algorithm for string matching and the LZ77 algorithm for data compression.
* The choice of base and modulus in the rolling hash function affects the algorithm's performance and accuracy.
* Implementing the Rabin-Karp algorithm in practice requires considering factors such as hash collisions and string encoding.

## Senior interview checkpoint

**Prompt:** Compare monotonic queue vs heap for sliding-window max under high-throughput constraints.

**What a senior answer should include**

- Constraints first (traffic, latency, reliability, ownership boundaries).
- Tradeoffs with at least two viable alternatives.
- Failure modes, observability signals, and rollback plan.
- A measurable success criterion after rollout.
