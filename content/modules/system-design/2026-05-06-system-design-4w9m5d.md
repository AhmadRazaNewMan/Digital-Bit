# Rate Limiting: Token Bucket vs Leaky Bucket
## What
Rate limiting is a technique used to control the amount of traffic that is sent or received by a system within a given time period. It helps prevent overloading, reduces the risk of denial-of-service (DoS) attacks, and ensures that resources are allocated fairly among users. Two popular algorithms for rate limiting are the Token Bucket and Leaky Bucket.

## Why
The Token Bucket and Leaky Bucket algorithms are used to implement rate limiting because they provide a way to manage the rate at which requests are processed. The Token Bucket algorithm is more flexible and allows for bursts of traffic, while the Leaky Bucket algorithm is more suitable for applications where a constant rate is required. Understanding the differences between these algorithms is important for designing and implementing effective rate limiting systems.

## How
The Token Bucket algorithm works by adding tokens to a bucket at a constant rate. Each request consumes one token, and if there are no tokens available, the request is blocked. The Leaky Bucket algorithm, on the other hand, works by adding requests to a bucket at a variable rate. If the bucket is full, new requests are blocked, and the bucket leaks at a constant rate. The choice of algorithm depends on the specific requirements of the system and the type of traffic it needs to handle.

## One exercise or command
To get a better understanding of how these algorithms work, try implementing a simple rate limiter using the Token Bucket algorithm in your preferred programming language. For example, you can use a queue to represent the bucket and add tokens to it at a constant rate. When a request is made, check if there are enough tokens in the bucket to process the request. If there are, remove the required number of tokens and process the request. If not, block the request.

## Further reading
* Token Bucket algorithm: 
  * Advantages: allows for bursts of traffic, flexible
  * Disadvantages: can be complex to implement, requires careful tuning of parameters
* Leaky Bucket algorithm: 
  * Advantages: simple to implement, provides a constant rate
  * Disadvantages: does not allow for bursts of traffic, can be less flexible
* Comparison of rate limiting algorithms: 
  * Token Bucket vs Leaky Bucket: which one to use and when
  * Other rate limiting algorithms: sliding window, fixed window
* Implementing rate limiting in practice: 
  * Using libraries and frameworks: examples and tutorials
  * Best practices: tuning parameters, handling edge cases

## Senior interview checkpoint

**Prompt:** Design a rate limiter that supports both global and per-user quotas.

**What a senior answer should include**

- Constraints first (traffic, latency, reliability, ownership boundaries).
- Tradeoffs with at least two viable alternatives.
- Failure modes, observability signals, and rollback plan.
- A measurable success criterion after rollout.
