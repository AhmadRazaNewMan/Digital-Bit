# Health Checks: Liveness vs Readiness
## What
Health checks are used to determine the status of a container or application in a Kubernetes environment. There are two types of health checks: liveness and readiness. Liveness checks determine if an application is running and responding correctly, while readiness checks determine if an application is ready to receive traffic.

## Why
The difference between liveness and readiness checks is crucial in a Kubernetes environment. Liveness checks help to detect if an application is running and responding correctly, and if not, the container is restarted. Readiness checks, on the other hand, help to detect if an application is ready to receive traffic, and if not, the container is not sent traffic until it is ready.

## How
To implement liveness and readiness checks in a Kubernetes environment, you can use probes. Probes are used to perform health checks on a container. There are three types of probes: HTTP, TCP, and Exec. HTTP probes send an HTTP request to the container and check the response. TCP probes attempt to establish a TCP connection to the container. Exec probes run a command inside the container and check the exit code.

## One exercise or command
To illustrate the difference between liveness and readiness checks, consider a simple web application that takes some time to start up. You can use the following command to create a pod with liveness and readiness checks:
```bash
kubectl create pod mypod --image=nginx --port=80 --liveness-probe=http://:80/ --readiness-probe=http://:80/healthz
```
In this example, the liveness probe checks if the web server is responding correctly, and the readiness probe checks if the web server is ready to receive traffic.

## Further reading
* Kubernetes documentation on [liveness and readiness probes](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/)
* Kubernetes documentation on [container probes](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.24/#probe-v1-core)
* Example of using [liveness and readiness probes in a deployment](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/#define-a-liveness-command)
