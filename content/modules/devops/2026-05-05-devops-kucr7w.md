# Immutable Artifacts vs Mutable Servers
## What
Immutable artifacts refer to software packages or images that cannot be modified once they are built. This approach ensures consistency and reliability across different environments. On the other hand, mutable servers are those that can be modified after deployment, which may lead to configuration drift and inconsistencies.

## Why
Using immutable artifacts is essential in a devops setup because it allows for easier rollbacks, improved security, and reduced debugging time. When an issue arises, it's easier to identify the problem and revert to a previous version. Additionally, immutable artifacts promote a culture of automation and continuous integration, reducing the risk of human error.

## How
To achieve immutable artifacts, devops teams can use containerization tools like Docker, which creates an image of the application and its dependencies. This image is then used to deploy the application to different environments. Another approach is to use package managers like apt or yum to create reproducible packages. Configuration management tools like Ansible or Puppet can also be used to ensure that servers are provisioned consistently.

## One exercise or command
Try building a Docker image for a simple web application using the following command: `docker build -t my-web-app .` This command creates a Docker image with the name `my-web-app` from the instructions in the `Dockerfile` in the current directory.

## Further reading
* Key benefits of immutable infrastructure:
  * Improved security and compliance
  * Reduced debugging time
  * Easier rollbacks and rollouts
  * Increased consistency across environments
* Tools for creating immutable artifacts:
  * Docker
  * Kubernetes
  * Ansible
  * Puppet
* Best practices for implementing immutable infrastructure:
  * Use version control for infrastructure code
  * Automate provisioning and deployment
  * Monitor and log changes to infrastructure
  * Use continuous integration and continuous deployment (CI/CD) pipelines

## Senior interview checkpoint

**Prompt:** Draft a rollback plan for failed blue-green deployment with partial data migrations.

**What a senior answer should include**

- Constraints first (traffic, latency, reliability, ownership boundaries).
- Tradeoffs with at least two viable alternatives.
- Failure modes, observability signals, and rollback plan.
- A measurable success criterion after rollout.
