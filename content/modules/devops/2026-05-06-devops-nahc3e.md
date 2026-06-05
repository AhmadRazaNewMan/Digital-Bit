# Secrets Rotation Without Downtime
## What
Secrets rotation without downtime refers to the process of updating sensitive information, such as passwords or API keys, in a system without interrupting its normal operation. This is crucial in ensuring the security and reliability of applications, especially those that handle sensitive user data.

## Why
Rotating secrets is essential for maintaining the security of systems, as it reduces the risk of data breaches and unauthorized access. If a secret is compromised, rotating it quickly can minimize the damage. Moreover, many regulatory compliance frameworks, such as PCI-DSS and HIPAA, require regular rotation of secrets.

## How
To rotate secrets without downtime, several strategies can be employed:
* Implementing a rolling update approach, where a new version of the application with the updated secret is deployed alongside the old version, and traffic is gradually shifted to the new version.
* Using a secrets manager, such as HashiCorp's Vault or AWS Secrets Manager, which can securely store and manage secrets, and provide features like automatic rotation and revocation.
* Utilizing a service discovery mechanism, such as DNS or a load balancer, to redirect traffic to a new instance of the application with the updated secret.

## One exercise or command
To demonstrate the concept of secrets rotation, consider a simple example using AWS Secrets Manager. The following command can be used to create a new secret and rotate it:
```bash
aws secretsmanager create-secret --name mysecret --secret-string file://secret.json
```
Assuming `secret.json` contains the new secret value.

## Further reading
* Best practices for secrets management: https://www.hashicorp.com/blog/best-practices-for-secrets-management
* AWS Secrets Manager documentation: https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html
* HashiCorp Vault documentation: https://www.vaultproject.io/docs 
* PCI-DSS guidelines for secrets management: https://www.pcisecuritystandards.org/document_library 
* HIPAA guidelines for secrets management: https://www.hhs.gov/hipaa/for-professionals/security/guidance/index.html

## Senior interview checkpoint

**Prompt:** Draft a rollback plan for failed blue-green deployment with partial data migrations.

**What a senior answer should include**

- Constraints first (traffic, latency, reliability, ownership boundaries).
- Tradeoffs with at least two viable alternatives.
- Failure modes, observability signals, and rollback plan.
- A measurable success criterion after rollout.
