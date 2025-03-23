---
title: IBM Db2 Database Locking
lang: en
layout: post
audio: false
translated: false
generated: true
---

Locking is a fundamental mechanism in any relational database management system (RDBMS), including IBM Db2, to ensure data consistency and integrity when multiple users or applications are accessing and modifying the same data concurrently. This tutorial will delve into the details of Db2 locking, covering how it works, row and table locks, potential problems like deadlocks, and strategies for avoidance and resolution, along with Java code examples.

### 1. How Locking Works in Db2

The primary goal of locking is to prevent data corruption that could occur if multiple transactions were to simultaneously modify the same data. Db2 employs a sophisticated lock manager that automatically manages locks on various database resources.

Here's a simplified overview of how it works:

* **Lock Request:** When a transaction needs to access or modify data, it implicitly or explicitly requests a lock on the relevant resource (e.g., a row, a table).
* **Lock Granting:** The Db2 lock manager checks if the requested lock conflicts with any existing locks held by other transactions.
    * If there are no conflicting locks, the lock is granted to the requesting transaction.
    * If there are conflicting locks, the requesting transaction may have to wait until the existing locks are released.
* **Lock Modes:** Db2 uses different lock modes to control the level of access granted. Common lock modes include:
    * **Shared (S) Lock:** Allows multiple transactions to read the same data concurrently but prevents any transaction from modifying it.
    * **Exclusive (X) Lock:** Allows only one transaction to access and modify the data. No other transaction can hold any type of lock on the same data.
    * **Update (U) Lock:** Used when a transaction intends to update a row. It's compatible with shared locks but not with other update or exclusive locks. It's often acquired during the read phase of an update operation.
* **Lock Duration:** Locks are typically held for the duration of a transaction. Once the transaction is committed or rolled back, all the locks held by that transaction are released.

### 2. Row Locks vs. Table Locks

Db2 can apply locks at different granularities, primarily at the row level and the table level. The choice between row and table locks depends on various factors, including the database configuration, the type of operation being performed, and the isolation level of the transaction.

#### 2.1. Row Locks

* **Granularity:** The lock is placed on a specific row within a table.
* **Concurrency:** Row-level locking generally allows for higher concurrency because different transactions can access and modify different rows within the same table simultaneously.
* **Overhead:** Managing a large number of row locks can introduce some overhead to the system.
* **When Used:** Db2 often uses row-level locking for operations that affect a small number of rows, such as individual `SELECT`, `INSERT`, `UPDATE`, and `DELETE` statements.

#### 2.2. Table Locks

* **Granularity:** The lock is placed on the entire table.
* **Concurrency:** Table-level locking significantly restricts concurrency, as only one transaction can access the table at a time (depending on the lock mode). Other transactions trying to access the same table will have to wait.
* **Overhead:** Table locks have lower overhead compared to managing numerous row locks.
* **When Used:** Db2 might escalate to table-level locking in the following scenarios:
    * Operations that affect a large portion of the table (e.g., `ALTER TABLE`, `DROP TABLE`, `TRUNCATE TABLE`).
    * Certain utility operations like backups or reorganizations.
    * If lock escalation occurs due to a large number of row locks being held by a single transaction (this is configurable).
    * When the transaction isolation level dictates it (e.g., Repeatable Read with certain operations).

**Lock Escalation:** Db2 has a mechanism called lock escalation where it can automatically promote row locks to a table lock if a transaction holds a certain threshold of row locks on the same table. This is done to reduce the overhead of managing a large number of fine-grained locks. The thresholds for lock escalation are configurable at the database or table level.

### 3. Problems Caused by Locking

While locking is essential for data consistency, it can also lead to performance issues and concurrency problems:

* **Blocking:** When a transaction holds a lock on a resource, other transactions that need to access the same resource in a conflicting mode will be blocked until the lock is released. This can lead to delays and reduced throughput.
* **Deadlocks:** A deadlock occurs when two or more transactions are blocked indefinitely, each waiting for a lock held by one of the others. This creates a circular dependency.

### 4. Transaction with Deadlock

Let's illustrate how a deadlock can occur with two transactions (Transaction A and Transaction B) accessing two resources (Row X and Row Y):

**Scenario:**

1.  **Transaction A** acquires an exclusive lock on **Row X**.
2.  **Transaction B** acquires an exclusive lock on **Row Y**.
3.  **Transaction A** attempts to acquire an exclusive lock on **Row Y**, but it's held by Transaction B. Transaction A is blocked.
4.  **Transaction B** attempts to acquire an exclusive lock on **Row X**, but it's held by Transaction A. Transaction B is blocked.

At this point, neither transaction can proceed because each is waiting for the other to release its lock. This is a deadlock.

**Db2 Deadlock Detection and Resolution:**

Db2 has a deadlock detector that periodically checks for such circular dependencies. When a deadlock is detected, Db2 will choose one of the involved transactions as the **victim** and roll it back. The transaction that is rolled back will receive an error (typically an SQLCODE indicating a deadlock), and it will need to be resubmitted by the application. The locks held by the victim transaction are released, allowing the other transaction(s) to proceed.

### 5. How to Avoid Deadlocks

Deadlocks can be detrimental to application performance and availability. Here are some strategies to minimize the occurrence of deadlocks:

* **Access Resources in the Same Order:** If multiple transactions frequently access the same set of resources, ensure that they access them in the same order. This can prevent the circular dependency that leads to deadlocks. For example, if both transactions need to access Row X and Row Y, make sure both always try to acquire the lock on Row X first, then Row Y.
* **Keep Transactions Short:** Shorter transactions hold locks for a shorter duration, reducing the window of opportunity for deadlocks to occur. Break down long-running transactions into smaller, more manageable units if possible.
* **Use Appropriate Isolation Levels:** The transaction isolation level determines the degree to which a transaction is isolated from the effects of other transactions. Higher isolation levels (e.g., Serializable, Repeatable Read) can increase the likelihood of deadlocks because they hold locks for longer periods. Consider using lower isolation levels (e.g., Read Committed, Read Uncommitted) if your application's consistency requirements allow it. Be aware of the trade-offs between isolation and concurrency.
* **Avoid User Interaction Within Transactions:** If a transaction involves user input or other external operations that can take an unpredictable amount of time, it's best to perform these operations outside the transaction boundaries. Holding locks while waiting for user input significantly increases the risk of blocking and deadlocks.
* **Use `SELECT FOR UPDATE` Carefully:** The `SELECT FOR UPDATE` statement acquires exclusive locks on the selected rows, preventing other transactions from modifying them. While useful in certain scenarios, overuse can increase contention and the potential for deadlocks. Use it only when you intend to update the selected rows within the same transaction.
* **Set Appropriate Lock Timeout Values:** Db2 allows you to configure lock timeout values. If a transaction cannot acquire a lock within the specified timeout period, it will receive an error instead of waiting indefinitely. This can help prevent indefinite blocking due to deadlocks, although it doesn't prevent the deadlock itself. The application will need to handle the timeout error and potentially retry the operation.
* **Optimize Queries:** Inefficient queries can take longer to execute and hold locks for longer periods, increasing the chance of deadlocks. Ensure your queries are well-indexed and optimized.

### 6. How to Fix Deadlocks

While the goal is to avoid deadlocks, they can still occur in complex systems. Here's how to handle them:

* **Application-Level Retry Logic:** The most common way to handle deadlocks is to implement retry logic in your application. When a transaction is rolled back due to a deadlock (indicated by a specific SQLCODE, such as -911 with reason code 2), the application should wait for a short period and then automatically retry the transaction. The retry mechanism should include a limit on the number of retries to prevent infinite loops.
* **Logging and Monitoring:** Implement proper logging to track deadlock occurrences. Monitoring database performance and identifying patterns of deadlocks can help in diagnosing the root cause and implementing preventative measures.
* **Analyze Deadlock Information:** Db2 often provides information about the transactions and resources involved in a deadlock. Analyzing this information can help you understand the sequence of events that led to the deadlock and identify potential areas for optimization or code changes.

### 7. Java Code Examples

Here's a Java code snippet demonstrating how to interact with a Db2 database and handle potential `SQLException`, including those indicating a deadlock:

```java
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

public class Db2LockingExample {

    private static final String DB_URL = "jdbc:db2://<hostname>:<port>/<database>";
    private static final String DB_USER = "<username>";
    private static final String DB_PASSWORD = "<password>";

    public static void main(Stringargs) {
        try {
            Class.forName("com.ibm.db2.jcc.DB2Driver");
        } catch (ClassNotFoundException e) {
            System.err.println("DB2 JDBC driver not found.");
            return;
        }

        // Simulate two concurrent transactions
        Thread transaction1 = new Thread(() -> performTransaction(1));
        Thread transaction2 = new Thread(() -> performTransaction(2));

        transaction1.start();
        transaction2.start();

        try {
            transaction1.join();
            transaction2.join();
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }
    }

    public static void performTransaction(int transactionId) {
        Connection conn = null;
        PreparedStatement pstmt1 = null;
        PreparedStatement pstmt2 = null;

        try {
            conn = DriverManager.getConnection(DB_URL, DB_USER, DB_PASSWORD);
            conn.setAutoCommit(false); // Start a transaction

            System.out.println("Transaction " + transactionId + ": Starting...");

            // Simulate accessing resources in a different order to potentially cause a deadlock
            if (transactionId == 1) {
                pstmt1 = conn.prepareStatement("SELECT * FROM accounts WHERE account_id = ? FOR UPDATE");
                pstmt1.setInt(1, 101);
                ResultSet rs1 = pstmt1.executeQuery();
                if (rs1.next()) {
                    System.out.println("Transaction " + transactionId + ": Locked account 101");
                    // Simulate some work
                    Thread.sleep(100);
                    pstmt2 = conn.prepareStatement("UPDATE accounts SET balance = balance - 10 WHERE account_id = ?");
                    pstmt2.setInt(1, 101);
                    pstmt2.executeUpdate();
                    System.out.println("Transaction " + transactionId + ": Updated account 101");

                    pstmt2 = conn.prepareStatement("SELECT * FROM accounts WHERE account_id = ? FOR UPDATE");
                    pstmt2.setInt(1, 102);
                    ResultSet rs2 = pstmt2.executeQuery();
                    if (rs2.next()) {
                        System.out.println("Transaction " + transactionId + ": Locked account 102");
                        pstmt2 = conn.prepareStatement("UPDATE accounts SET balance = balance + 10 WHERE account_id = ?");
                        pstmt2.setInt(1, 102);
                        pstmt2.executeUpdate();
                        System.out.println("Transaction " + transactionId + ": Updated account 102");
                    }
                }
            } else {
                pstmt1 = conn.prepareStatement("SELECT * FROM accounts WHERE account_id = ? FOR UPDATE");
                pstmt1.setInt(1, 102);
                ResultSet rs1 = pstmt1.executeQuery();
                if (rs1.next()) {
                    System.out.println("Transaction " + transactionId + ": Locked account 102");
                    Thread.sleep(100);
                    pstmt2 = conn.prepareStatement("UPDATE accounts SET balance = balance + 10 WHERE account_id = ?");
                    pstmt2.setInt(1, 102);
                    pstmt2.executeUpdate();
                    System.out.println("Transaction " + transactionId + ": Updated account 102");

                    pstmt2 = conn.prepareStatement("SELECT * FROM accounts WHERE account_id = ? FOR UPDATE");
                    pstmt2.setInt(1, 101);
                    ResultSet rs2 = pstmt2.executeQuery();
                    if (rs2.next()) {
                        System.out.println("Transaction " + transactionId + ": Locked account 101");
                        pstmt2 = conn.prepareStatement("UPDATE accounts SET balance = balance - 10 WHERE account_id = ?");
                        pstmt2.setInt(1, 101);
                        pstmt2.executeUpdate();
                        System.out.println("Transaction " + transactionId + ": Updated account 101");
                    }
                }
            }

            conn.commit();
            System.out.println("Transaction " + transactionId + ": Committed successfully.");

        } catch (SQLException e) {
            System.err.println("Transaction " + transactionId + ": Error occurred - " + e.getMessage());
            if (conn != null) {
                try {
                    conn.rollback();
                    System.out.println("Transaction " + transactionId + ": Rolled back.");
                    // Check for deadlock condition (SQLCODE -911, reason code 2)
                    if (e.getSQLState() != null && e.getSQLState().equals("40001") && e.getErrorCode() == -911 && e.getMessage().contains("Reason code 2")) {
                        System.out.println("Transaction " + transactionId + ": Deadlock detected. Consider retrying.");
                        // Implement retry logic here
                    }
                } catch (SQLException rollbackEx) {
                    System.err.println("Transaction " + transactionId + ": Error during rollback - " + rollbackEx.getMessage());
                }
            }
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        } finally {
            try {
                if (pstmt1 != null) pstmt1.close();
                if (pstmt2 != null) pstmt2.close();
                if (conn != null) conn.close();
            } catch (SQLException closeEx) {
                System.err.println("Error closing resources: " + closeEx.getMessage());
            }
        }
    }
}
```

**Explanation of the Java Code:**

1.  **Database Connection:** The code establishes a connection to the Db2 database using JDBC. You'll need to replace the placeholder connection details with your actual database information.
2.  **Simulating Concurrent Transactions:** Two threads are created, each running the `performTransaction` method. This simulates two concurrent transactions trying to access and modify data.
3.  **Transaction Management:** `conn.setAutoCommit(false)` is used to start an explicit transaction. `conn.commit()` commits the changes, and `conn.rollback()` rolls back the transaction in case of an error.
4.  **Accessing Resources in Different Orders:** The two transactions are designed to access the `accounts` table with `account_id` 101 and 102 in a different order using `SELECT * FROM accounts WHERE account_id = ? FOR UPDATE`. The `FOR UPDATE` clause acquires an exclusive lock on the selected rows. This creates a scenario where a deadlock might occur if both transactions try to lock both rows.
5.  **Simulating Work:** `Thread.sleep(100)` is used to simulate some processing time between acquiring the first lock and attempting to acquire the second lock, increasing the likelihood of a deadlock.
6.  **Handling `SQLException`:** The `catch` block catches any `SQLException` that might occur during the transaction.
7.  **Deadlock Detection:** Inside the `catch` block, the code checks for the specific SQLSTATE ("40001") and error code (-911) with a message containing "Reason code 2". This combination typically indicates a deadlock in Db2.
8.  **Retry Logic (Placeholder):** The code includes a comment indicating where you would implement retry logic if a deadlock is detected. In a real application, you would typically wait for a short period and then attempt to execute the transaction again.
9.  **Resource Cleanup:** The `finally` block ensures that database resources (statements and connection) are closed properly, even if an exception occurs.

**To run this code:**

1.  Make sure you have the IBM Db2 JDBC driver (`db2jcc4.jar` or similar) in your project's classpath.
2.  Replace the placeholder database connection details (`DB_URL`, `DB_USER`, `DB_PASSWORD`) with your actual Db2 database credentials.
3.  Create an `accounts` table in your Db2 database with columns like `account_id` (INT) and `balance` (DECIMAL).
4.  Run the Java code. You might observe that one of the transactions is rolled back due to a deadlock, and the error message will indicate this.

### 8. Conclusion

Understanding how locking works in IBM Db2 is crucial for building concurrent and reliable applications. By being aware of the different types of locks, the problems they can cause (especially deadlocks), and the strategies for avoidance and resolution, you can design your database interactions to minimize contention and ensure data integrity. Remember to implement robust error handling, including retry mechanisms for deadlock situations, in your applications.