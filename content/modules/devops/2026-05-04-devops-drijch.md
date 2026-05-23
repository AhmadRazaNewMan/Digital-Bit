# Health Checks: Liveness vs Readiness
## What
Health checks are crucial in ensuring the reliability and availability of applications in a DevOps environment. They are used to determine the status of an application or service, helping to identify if it's functioning as expected. Two primary types of health checks are liveness and readiness probes. Liveness checks verify if an application is running and responding, while readiness checks confirm if the application is ready to receive traffic.

## Why
Understanding the difference between liveness and readiness is essential for maintaining the health and efficiency of applications. Liveness checks help in restarting applications that have failed, while readiness checks prevent sending traffic to applications that are not fully initialized or are in the process of shutting down. This distinction is vital for preventing cascading failures and ensuring a better user experience.

## How
Implementing liveness and readiness checks involves configuring probes that periodically test the application's health. This can be done using HTTP requests, TCP connections, or command executions, depending on the application's requirements. For example, a web server might use an HTTP GET request to check liveness, while a database service might use a TCP connection to verify readiness.

## One exercise or command
To illustrate the concept, consider a simple example using Kubernetes, where you can define liveness and readiness probes for a pod:
```yml
apiVersion: v1
kind: Pod
metadata:
  name: example-pod
spec:
  containers:
  - name: example-container
    image: example-image
    livenessProbe:
      httpGet:
        path: /health
        port: 8080
      initialDelaySeconds: 15
      periodSeconds: 15
    readinessProbe:
      httpGet:
        path: /ready
        port: 8080
      initialDelaySeconds: 5
      periodSeconds: 5
```
This example demonstrates how to configure liveness and readiness probes for a container using HTTP GET requests.

## Further reading
* Kubernetes documentation on [liveness and readiness probes](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/)
* [Best practices for implementing health checks](https://aws.amazon.com/blogs/containers/monitoring-container-health-with-aws-ecs/)
* [Differences between liveness and readiness probes](https://www.datadoghq.com/blog/how-to-monitor-service-health-with-readiness-probes/)

## Senior interview checkpoint

**Prompt:** Design CI guardrails to prevent secret leaks and oversized images.

**What a senior answer should include**

- Constraints first (traffic, latency, reliability, ownership boundaries).
- Tradeoffs with at least two viable alternatives.
- Failure modes, observability signals, and rollback plan.
- A measurable success criterion after rollout.
