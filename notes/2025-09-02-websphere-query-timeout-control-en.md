---
title: WebSphere Query Timeout Thread Interruption Control
lang: en
layout: post
audio: false
translated: false
generated: true
image: false
---

In WebSphere Application Server, the `queryTimeoutInterruptProcessingMode` property is a **data source custom property** that controls how query timeouts are enforced when an SQL statement exceeds its configured `queryTimeout`.

Here’s how it works:

### Default Behavior

Normally, when a query timeout is reached, WebSphere calls the JDBC driver’s `Statement.cancel()` method. This only **sends a cancel request** to the database. Depending on the database and driver, the running SQL may or may not stop immediately. Sometimes it continues consuming resources on the database server until it finishes or until the DB itself decides to terminate it.

### Purpose of `queryTimeoutInterruptProcessingMode`

This property determines what WebSphere itself does **in addition to calling `Statement.cancel()`**:

* **When set to `true` (enabled):**

  * WebSphere **interrupts the thread** running the query after the timeout.
  * This means the application thread will stop waiting for the query, even if the database hasn’t finished canceling it.
  * Useful when you want to ensure application responsiveness and not have threads hanging indefinitely.
  * Downside: interrupting a thread can cause `SQLException`s or inconsistent states if the app or driver wasn’t designed to handle it.

* **When set to `false` (disabled, default):**

  * WebSphere **does not interrupt the thread**.
  * It relies only on `Statement.cancel()` and waits for the driver/database to handle cancellation.
  * Safer for app stability, but riskier for performance if the DB takes too long to cancel.

### Typical Use Cases

* **Enable (`true`)** if:

  * You have seen JDBC calls hanging even after timeout.
  * You want to guarantee that application threads are freed.
  * You are okay handling `InterruptedException`-like behavior or extra SQLExceptions in your app.

* **Keep Disabled (`false`)** if:

  * Your JDBC driver and DB reliably handle cancellations.
  * You don’t want to risk interrupting threads mid-processing.
  * Stability and clean DB-driver state are more important than fast thread release.

---

✅ **In short:**
`queryTimeoutInterruptProcessingMode=true` makes WebSphere forcibly break the waiting thread when query timeout is reached. `false` relies only on the DB driver to cancel the SQL. It’s a trade-off between responsiveness and stability.

---

Do you want me to also explain **how this interacts with `statementTimeout` and `connectionTimeout`** in WebSphere data sources? That way you’ll see the full picture of timeout handling.