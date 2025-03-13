---
title: How Locking Works in IBM Db2 Database
lang: en
layout: post
audio: false
translated: false
generated: true
---

In IBM Db2, locking is a mechanism used to manage concurrent access to data by multiple transactions, ensuring data consistency and preventing conflicts that could lead to errors or inconsistencies. When a transaction performs an operation like updating a row, Db2 employs locks to control how other transactions can interact with the affected data.

#### Locking During an Update Operation
When a row is updated in Db2, the database typically acquires an **exclusive lock** on that row. An exclusive lock prevents other transactions from reading or modifying the locked row until the update transaction either commits or rolls back. This ensures that the data remains consistent during the update process.

#### Does a Select on the Same Table Wait?
Whether a `SELECT` operation on the same table waits for the update to finish depends on which row the `SELECT` is trying to access:

- **If the `SELECT` targets the row being updated**: The `SELECT` will wait until the update transaction completes (commits or rolls back). This is because the exclusive lock on the updated row blocks other transactions from reading it, assuming a default isolation level like **Cursor Stability (CS)**, which is common in Db2. In CS, a `SELECT` typically acquires a **shared lock** to read a row, but this shared lock is incompatible with the exclusive lock held by the update, causing the `SELECT` to wait.
- **If the `SELECT` targets a different row**: The `SELECT` will not wait and can proceed immediately. This is because the lock is applied only to the specific row being updated, not the entire table, allowing other rows to remain accessible.

However, the exact behavior can vary slightly depending on the **isolation level**:
- In **Uncommitted Read (UR)**, a `SELECT` can read the row being updated without waiting, even if it’s uncommitted (a "dirty read"), but this is rare in practice due to consistency concerns.
- In higher isolation levels like **Read Stability (RS)** or **Repeatable Read (RR)**, the `SELECT` might wait even longer or acquire additional locks, depending on the operation.

Since the query doesn’t specify an isolation level, we’ll assume the default behavior (typically Cursor Stability in Db2), where a `SELECT` waits only if it tries to access the locked row.

#### Row-Level Lock or Table-Level Lock?
Db2 uses **row-level locking** by default when updating a row. This means that only the specific row being updated is locked, not the entire table. Row-level locking provides higher concurrency, as other transactions can still access different rows in the same table without interference.

- **Default Behavior**: When you create a table in Db2 without specifying the `LOCKSIZE` parameter, it defaults to `ROW`. This applies to Db2 for Linux, UNIX, and Windows (LUW), which is the most common context unless specified otherwise (e.g., Db2 on z/OS might have different defaults, but row-level locking is still typical).
- **Lock Escalation**: In rare cases, Db2 may escalate locks from row-level to table-level if a transaction acquires too many row locks, to reduce memory overhead. However, for a single row update, escalation is unlikely.
- **Explicit Control**: You can override the default by setting `LOCKSIZE` to `TABLE` when creating or altering a table, but this is not the norm for typical operations.

Thus, for a standard update of a single row, Db2 employs **row-level locking**, not table-level locking.

### Summary
- **Locking Mechanism**: Db2 uses row-level locking by default when updating a row, applying an exclusive lock to the specific row.
- **Select Behavior**: A `SELECT` on the same table will wait only if it attempts to access the row being updated. If it targets other rows, it proceeds without delay.
- **Lock Type**: It is **row-level locking**, not table-level, under default settings.

This row-level approach ensures efficient concurrency, allowing multiple transactions to operate on different rows simultaneously while maintaining data integrity for the row being modified.