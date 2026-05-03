# Rolling Deploys and Failure Budgets
## What
Rolling deploys and failure budgets are essential concepts in DevOps that enable teams to deploy software changes with minimal disruption to users. A rolling deploy involves gradually replacing instances of an old version with a new one, while a failure budget refers to the acceptable amount of failures or errors that can occur during the deployment process.

## Why
Implementing rolling deploys and failure budgets is crucial for maintaining system reliability and availability. By gradually rolling out changes, teams can quickly identify and address issues before they affect a large number of users. Failure budgets help teams prioritize reliability and set realistic expectations for system performance.

## How
To implement rolling deploys and failure budgets, teams can follow these general steps:
- Monitor system performance and set a failure budget based on acceptable error rates
- Automate the deployment process using tools like Kubernetes or Ansible
- Gradually roll out changes to a small subset of users or instances
- Monitor the deployment and adjust as needed to stay within the failure budget

## One exercise or command
Try using the following command to roll out a new version of a deployment using Kubernetes: `kubectl rollout update deployment <deployment-name> --image=<new-image-name>`

## Further reading
* Learn more about Kubernetes rolling updates: https://kubernetes.io/docs/tutorials/kubernetes-basics/update/update-intro/
* Understand failure budgets and how to set them: https://sre.google/sre-book/failure-budgets/
* Explore Ansible deploy playbooks: https://docs.ansible.com/ansible/latest/user_guide/playbooks.html
