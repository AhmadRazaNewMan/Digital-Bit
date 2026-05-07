# Rate Limiting: Per User vs Per IP
## What
Rate limiting is a technique used to control the number of requests a user or IP address can send to a server within a certain time frame. This is done to prevent abuse, denial-of-service (DoS) attacks, and to ensure fair usage of resources. There are two common approaches to rate limiting: per user and per IP.

## Why
Per user rate limiting is more secure as it takes into account authenticated users, making it harder for attackers to bypass the limit by switching IPs. On the other hand, per IP rate limiting is simpler to implement and can be effective against brute-force attacks. However, it can lead to false positives, where multiple legitimate users sharing the same IP are limited.

## How
To implement rate limiting per user, you need to track the number of requests made by each user and store this information in a database or cache. For per IP rate limiting, you can use the IP address of the incoming request to track and limit the number of requests. You can use algorithms such as token bucket or leaky bucket to implement rate limiting.

## One exercise or command
Try implementing a simple rate limiter using the token bucket algorithm, where each user has a bucket that can hold a certain number of tokens. Each request consumes one token, and the bucket is refilled at a certain rate.

## Further reading
* Key differences between per user and per IP rate limiting
* Token bucket algorithm for rate limiting
* Leaky bucket algorithm for rate limiting
* Implementing rate limiting using caching mechanisms like Redis or Memcached
* Best practices for rate limiting to prevent abuse and ensure fair usage of resources
