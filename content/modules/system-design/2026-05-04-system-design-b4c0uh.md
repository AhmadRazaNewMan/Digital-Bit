# Rate Limiting: Token Bucket vs Leaky Bucket
## What
Rate limiting is a technique used to control the amount of traffic that is sent or received by a system. It is used to prevent overload, reduce latency, and prevent abuse. Two popular algorithms for rate limiting are the token bucket algorithm and the leaky bucket algorithm.

## Why
The token bucket and leaky bucket algorithms are used to limit the rate at which requests are processed by a system. The main difference between the two algorithms is how they handle bursts of traffic. The token bucket algorithm allows for bursts of traffic by accumulating tokens over time, while the leaky bucket algorithm does not allow for bursts and instead drops packets when the bucket is full.

## How
The token bucket algorithm works by adding tokens to a bucket at a constant rate. Each request requires a certain number of tokens to be processed. If there are enough tokens in the bucket, the request is processed and the tokens are removed from the bucket. If there are not enough tokens, the request is blocked until there are enough tokens. The leaky bucket algorithm works by adding packets to a bucket at a variable rate. The bucket leaks at a constant rate, and if the bucket is full, packets are dropped.

## One exercise or command
To implement rate limiting using the token bucket algorithm, you can use the following steps:
* Create a bucket with a maximum capacity
* Add tokens to the bucket at a constant rate
* For each request, check if there are enough tokens in the bucket
* If there are enough tokens, process the request and remove the tokens from the bucket
* If there are not enough tokens, block the request until there are enough tokens

## Further reading
* Key characteristics of token bucket algorithm:
  + allows for bursts of traffic
  + accumulates tokens over time
  + suitable for applications that require a high degree of flexibility
* Key characteristics of leaky bucket algorithm:
  + does not allow for bursts of traffic
  + drops packets when the bucket is full
  + suitable for applications that require a high degree of predictability
* Comparison of token bucket and leaky bucket algorithms:
  + token bucket algorithm is more flexible, but can lead to overload if not properly configured
  + leaky bucket algorithm is more predictable, but can lead to packet loss if the bucket is too small

## Senior interview checkpoint

**Prompt:** Design a rate limiter that supports both global and per-user quotas.

**What a senior answer should include**

- Constraints first (traffic, latency, reliability, ownership boundaries).
- Tradeoffs with at least two viable alternatives.
- Failure modes, observability signals, and rollback plan.
- A measurable success criterion after rollout.
