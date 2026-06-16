# Transaction Isolation Anomalies
## What
Transaction isolation anomalies refer to inconsistencies that can occur when multiple transactions access shared data in a database management system (DBMS). Two common types of anomalies are dirty read and phantom read. A dirty read occurs when a transaction reads data that has been modified by another transaction but not yet committed. A phantom read occurs when a transaction reads data that is being inserted or deleted by another transaction.

## Why
These anomalies can lead to incorrect results, data inconsistencies, and errors in the database. Understanding transaction isolation anomalies is crucial to ensure data integrity and consistency in a DBMS. The level of isolation determines how much a transaction is affected by other transactions.

## How
To prevent or minimize these anomalies, DBMS uses various isolation levels, such as:
* READ UNCOMMITTED: allows dirty reads
* READ COMMITTED: prevents dirty reads
* REPEATABLE READ: prevents dirty reads and some phantom reads
* SERIALIZABLE: prevents all dirty reads and phantom reads
Each isolation level has its own trade-offs between consistency and performance.

## One exercise or command
To demonstrate a dirty read, consider the following example: 
Suppose we have two transactions, T1 and T2. T1 updates a row, but does not commit. T2 then reads the updated row. If T1 rolls back, T2 will have read an inconsistent value. This can be simulated using SQL commands:
```sql
-- T1
BEGIN TRANSACTION;
UPDATE accounts SET balance = 100 WHERE id = 1;

-- T2
SELECT * FROM accounts WHERE id = 1;

-- T1
ROLLBACK;
```
In this example, T2 reads the updated balance, but it is rolled back by T1.

## Further reading
* Concurrency control mechanisms in DBMS
* Isolation levels in popular DBMS (e.g., MySQL, PostgreSQL)
* Locking mechanisms to prevent transaction isolation anomalies
* Comparison of different isolation levels and their implications on performance and consistency
* Real-world examples of transaction isolation anomalies and how to avoid them

## Senior interview checkpoint

**Prompt:** Explain how isolation level affects deadlocks in write-heavy workloads.

**What a senior answer should include**

- Constraints first (traffic, latency, reliability, ownership boundaries).
- Tradeoffs with at least two viable alternatives.
- Failure modes, observability signals, and rollback plan.
- A measurable success criterion after rollout.
