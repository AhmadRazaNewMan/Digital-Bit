# Rolling Deploys and Failure Budgets
## What
Rolling deploys and failure budgets are essential concepts in DevOps that enable teams to deliver software updates and changes with minimal disruption to users. Rolling deploys involve gradually replacing instances of an old version of an application with new instances running the updated version. Failure budgets, on the other hand, refer to the acceptable amount of failure or downtime that a system can tolerate while still meeting its service level objectives (SLOs).

## Why
The combination of rolling deploys and failure budgets is crucial for several reasons. Firstly, rolling deploys minimize the risk of deploying new changes by gradually introducing them to the production environment, allowing for quicker rollback in case of issues. Secondly, failure budgets help teams prioritize reliability work and allocate resources effectively to ensure the system remains within its acceptable failure threshold. This approach balances the need for continuous delivery with the requirement for high system reliability.

## How
Implementing rolling deploys and failure budgets involves several steps:
- **Monitoring and Feedback**: Establish comprehensive monitoring to quickly identify issues during a roll-out.
- **Automated Rollback**: Implement automated rollback processes to quickly revert to a stable version if issues arise.
- **Failure Budget Calculation**: Calculate the failure budget based on historical data, SLOs, and business requirements.
- **Prioritization**: Prioritize features and fixes based on their impact on the failure budget and overall system reliability.

## One exercise or command
To practice implementing a rolling deploy, consider using Kubernetes, where you can use the `kubectl rollout` command to manage the deployment of new versions of an application. For example, `kubectl rollout status deployment/my-deployment` can be used to monitor the progress of a rolling update.

## Further reading
* **SRE Book**: Start with the Google SRE book, which provides detailed insights into how Google approaches service reliability, including failure budgets and rolling deploys.
* **Kubernetes Documentation**: Refer to Kubernetes documentation for rolling updates to understand how to implement rolling deploys in a Kubernetes environment.
* **Failure Budget Articles**: Look for articles and case studies on how different companies calculate and manage their failure budgets to gain practical insights.
* **Service Level Objectives (SLOs)**: Study how to set effective SLOs, as they are crucial for determining the acceptable failure budget for your system.
