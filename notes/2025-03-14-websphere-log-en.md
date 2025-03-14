---
title: WebSphere Liberty Logging
lang: en
layout: post
audio: false
translated: false
generated: true
---

In WebSphere Liberty Server, **console.log** and **messages.log** are two distinct log files with different purposes:

- **console.log**: This file captures the standard output and standard error streams from the Java Virtual Machine (JVM) process. It includes messages directly written by the JVM (e.g., verbose garbage collection output) and any messages that applications write to `System.out` or `System.err` (if configured). It is designed for human readability and is reset each time the server restarts.

- **messages.log**: This file contains all messages (except trace messages) written or captured by the server's logging component. It includes informational messages, warnings, errors, and audit messages from both the server and applications. Each message is timestamped and includes the thread ID, making it valuable for detailed analysis and debugging.

In short, **console.log** focuses on JVM and application output for easy reading, while **messages.log** provides server and application messages with metadata for in-depth troubleshooting.