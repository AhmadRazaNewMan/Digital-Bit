# Rate Limiting: Token Bucket vs Leaky Bucket
## What
Rate limiting is a technique used to control the frequency of requests to a system, preventing it from being overwhelmed. Two common algorithms used for rate limiting are the token bucket and leaky bucket algorithms. The token bucket algorithm is based on the idea of a bucket that can hold a certain number of tokens, which are added to the bucket at a constant rate. The leaky bucket algorithm, on the other hand, is based on the idea of a bucket that leaks at a constant rate.

## Why
The token bucket and leaky bucket algorithms are used to prevent systems from being overwhelmed by a large number of requests in a short period of time. They help to ensure that the system can handle the requests in a fair and efficient manner. The token bucket algorithm is more flexible and allows for bursts of traffic, while the leaky bucket algorithm is more strict and does not allow for bursts.

## How
The token bucket algorithm works by adding tokens to the bucket at a constant rate. When a request is made, a token is removed from the bucket. If the bucket is empty, the request is blocked until a token is added. The leaky bucket algorithm works by allowing requests to be made as long as the bucket is not full. The bucket leaks at a constant rate, and if the bucket is full, requests are blocked until the bucket leaks.

## One exercise or command
To implement a simple token bucket algorithm, you can use the following command: `token_bucket = []; token_rate = 5; token_capacity = 10;` and then add tokens to the bucket at the specified rate and remove tokens when requests are made.

## Further reading
* The token bucket algorithm is more suitable for systems that need to allow for bursts of traffic
* The leaky bucket algorithm is more suitable for systems that need to ensure a constant rate of requests
* Both algorithms can be used together to provide a more flexible and efficient rate limiting system
* Rate limiting can be used in a variety of systems, including web servers, databases, and networks
* The choice of algorithm depends on the specific requirements of the system and the type of traffic it needs to handle

## Senior interview checkpoint

**Prompt:** Design a rate limiter that supports both global and per-user quotas.

**What a senior answer should include**

- Constraints first (traffic, latency, reliability, ownership boundaries).
- Tradeoffs with at least two viable alternatives.
- Failure modes, observability signals, and rollback plan.
- A measurable success criterion after rollout.
