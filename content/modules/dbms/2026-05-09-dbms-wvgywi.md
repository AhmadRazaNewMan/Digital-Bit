# TODAY'S FOCUS: Sequential Scan vs Index Scan in Query Execution
## What
Database Management Systems (DBMS) execute queries using various methods to optimize performance. Two fundamental approaches are sequential scan and index scan. A sequential scan involves reading the entire table from disk, checking each row to see if it meets the query conditions. An index scan, on the other hand, uses an index to quickly locate specific rows that match the query conditions.

## Why
Understanding the difference between sequential and index scans is crucial for query optimization. Sequential scans can be slow for large tables, while index scans can significantly speed up query execution. However, creating and maintaining indexes can add overhead, so it's essential to use them judiciously.

## How
To determine whether a query uses a sequential scan or an index scan, you can use the EXPLAIN command in SQL. The EXPLAIN command shows the query execution plan, which includes the access method used (e.g., sequential scan or index scan). By analyzing the execution plan, you can identify performance bottlenecks and optimize your queries.

## One exercise or command
To illustrate the difference, consider a simple example:
```sql
EXPLAIN SELECT * FROM customers WHERE customer_id = 123;
```
This command will show the execution plan for the query, indicating whether a sequential scan or an index scan is used.

## Further reading
* Learn about different types of indexes (e.g., B-tree, hash) and their use cases
* Understand how to create and manage indexes in your DBMS
* Explore query optimization techniques, such as rewriting queries to use indexes effectively
* Study the EXPLAIN command and its output to analyze query execution plans
* Investigate the trade-offs between query performance and index maintenance overhead

## Senior interview checkpoint

**Prompt:** Explain how isolation level affects deadlocks in write-heavy workloads.

**What a senior answer should include**

- Constraints first (traffic, latency, reliability, ownership boundaries).
- Tradeoffs with at least two viable alternatives.
- Failure modes, observability signals, and rollback plan.
- A measurable success criterion after rollout.
