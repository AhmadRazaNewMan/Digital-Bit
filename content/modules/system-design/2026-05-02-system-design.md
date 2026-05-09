# Cache Stampede and Probabilistic Early Expiration
## What
Cache stampede, also known as cache thundering herd, is a phenomenon where multiple requests for the same data try to refresh a cache entry simultaneously, causing a surge in request traffic to the underlying system. This can lead to increased latency and resource utilization. Probabilistic early expiration is a strategy used to mitigate this issue by introducing randomness to the cache expiration time.

## Why
Cache stampede can occur when a popular cache entry expires, triggering a large number of requests to refresh the entry at the same time. This can cause significant strain on the system, leading to performance degradation and potentially even failures. Probabilistic early expiration helps to distribute the requests over time, reducing the likelihood of a cache stampede.

## How
To implement probabilistic early expiration, a random value is added to the cache expiration time. This random value is typically small compared to the overall expiration time, but it helps to spread out the requests to refresh the cache entry. When the cache entry expires, the system will refresh the entry, but the random value ensures that not all requests will expire at the same time.

## One exercise or command
Try implementing a simple cache system with probabilistic early expiration using a programming language of your choice. Use a random number generator to add a small random value (e.g., 1-10 seconds) to the cache expiration time. Measure the impact of this strategy on the system's performance under heavy load.

## Further reading
* Strategies for mitigating cache stampede:
  + Implementing probabilistic early expiration
  + Using a lease-based approach to cache expiration
  + Introducing a cache entry refresh queue to manage concurrent requests
* Cache expiration strategies:
  + Time To Live (TTL) based expiration
  + Least Recently Used (LRU) based expiration
  + Most Recently Used (MRU) based expiration
* Performance optimization techniques for cache systems:
  + Load balancing and traffic distribution
  + Request batching and coalescing
  + Asynchronous cache refresh and updates

## Senior interview checkpoint

**Prompt:** Explain cache invalidation strategy for hot keys with high write rates.

**What a senior answer should include**

- Constraints first (traffic, latency, reliability, ownership boundaries).
- Tradeoffs with at least two viable alternatives.
- Failure modes, observability signals, and rollback plan.
- A measurable success criterion after rollout.
