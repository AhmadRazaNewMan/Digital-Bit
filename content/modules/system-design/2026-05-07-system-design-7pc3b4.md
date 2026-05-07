# Cache Stampede and Probabilistic Early Expiration
## What
Cache stampede, also known as thundering herd, occurs when multiple requests try to access the same cache entry simultaneously, resulting in a surge of requests to the underlying system. This can happen when a popular cache entry expires, causing all waiting requests to flood the system with requests. Probabilistic early expiration is a technique used to mitigate cache stampede by introducing randomness in cache expiration times.

## Why
Cache stampede can lead to significant performance degradation, increased latency, and even system crashes. By introducing probabilistic early expiration, the system can avoid cache stampede by staggering the expiration times of cache entries. This technique helps to reduce the likelihood of multiple requests trying to access the same cache entry at the same time.

## How
To implement probabilistic early expiration, a random factor is introduced into the cache expiration time. This random factor can be a fixed time range, such as between 1-5 minutes, or a percentage of the total cache expiration time. When a cache entry is created, its expiration time is calculated by adding the random factor to the base expiration time. This ensures that cache entries expire at slightly different times, reducing the likelihood of cache stampede.

## One exercise or command
Try implementing a simple cache system with probabilistic early expiration using Python:
* Create a cache dictionary with a fixed expiration time (e.g., 60 seconds)
* Introduce a random factor (e.g., between 1-10 seconds) to the expiration time for each cache entry
* Test the cache system with multiple concurrent requests to observe the effect of probabilistic early expiration

## Further reading
* Learn about other cache stampede mitigation techniques, such as:
  + Using a lock or semaphore to synchronize access to cache entries
  + Implementing a least recently used (LRU) cache eviction policy
  + Using a cache hierarchical structure to reduce the load on the underlying system
* Explore the trade-offs between cache expiration time, random factor, and system performance
* Read about real-world examples of cache stampede and how they were mitigated in production systems
