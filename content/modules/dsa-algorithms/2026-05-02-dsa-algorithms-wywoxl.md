# Rolling Hash and Rabin–Karp for Substring Search
## What
Rolling hash and Rabin–Karp are algorithms used for substring search, which involves finding a given pattern within a text. The rolling hash technique allows for efficient comparison of strings by calculating a hash value for each substring of the text and comparing it with the hash value of the pattern. The Rabin–Karp algorithm utilizes rolling hash to search for a pattern in a text.

## Why
The Rabin–Karp algorithm is particularly useful when the pattern is relatively small compared to the text. It has an average time complexity of O(n+m), where n is the length of the text and m is the length of the pattern, making it efficient for substring search. Additionally, rolling hash enables fast comparison of strings, reducing the overall time complexity of the algorithm.

## How
The Rabin–Karp algorithm works as follows:
* Calculate the hash value of the pattern.
* Calculate the hash value of the first substring of the text with the same length as the pattern.
* Compare the hash values of the pattern and the substring. If they match, compare the strings character by character to confirm the match.
* If the hash values do not match, calculate the hash value of the next substring by removing the leading character and adding the next character.
* Repeat the comparison and hash value calculation until the end of the text is reached.

## One exercise or command
Implement the Rabin–Karp algorithm to search for the pattern "abc" in the text "abcdef".

## Further reading
* The Rabin–Karp algorithm is a variation of the string searching algorithm that uses hashing to find any substring in a text.
* It uses a rolling hash to quickly filter out positions of the text that cannot match the pattern, and then checks for a match at the remaining positions.
* Key advantages include:
  + Average time complexity of O(n+m)
  + Efficient for small patterns
  + Suitable for searching multiple patterns in a single pass
* Key disadvantages include:
  + Can have poor performance in the worst case (e.g., when all substrings have the same hash value)
  + Requires careful choice of hash function to minimize collisions

## Senior interview checkpoint

**Prompt:** Design an approach for top-K frequent items in a streaming system with memory limits.

**What a senior answer should include**

- Constraints first (traffic, latency, reliability, ownership boundaries).
- Tradeoffs with at least two viable alternatives.
- Failure modes, observability signals, and rollback plan.
- A measurable success criterion after rollout.
