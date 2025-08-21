---
title: DB2 JCC Timeout Behavior Comparison
lang: en
layout: post
audio: false
translated: false
generated: true
image: false
---

### Comparison of setQueryTimeout in DB2 JCC Driver Versions 4.17.29 and 4.19.66

The DB2 JCC driver (IBM Data Server Driver for JDBC and SQLJ) is a Type 4 JDBC driver used for connecting to DB2 databases. The versions you mentioned correspond to the following:

- 4.17.29: Associated with DB2 10.5 Fix Pack 3 (FP3), an older fix level from around 2014.
- 4.19.66: Associated with DB2 10.5 Fix Pack 8 (FP8), a later fix level within the same DB2 release.

The setQueryTimeout method is a standard JDBC Statement method to set a timeout in seconds for query execution. It is supported in both versions since they are Type 4 drivers (db2jcc4.jar), but there are nuances in behavior, especially in certain environments or with DB2 on z/OS.

#### Differences in Behavior
- **General Behavior**: In both versions, setQueryTimeout is supported for execute, executeUpdate, and executeQuery methods. However, its effectiveness can depend on the environment (e.g., application server like WebSphere vs. Tomcat) and the DB2 platform (LUW vs. z/OS). The driver uses a timer thread to interrupt long-running queries.
- **Property Dependencies**: The property queryTimeoutInterruptProcessingMode controls how the timeout is enforced:
  - Value 1 (default): Uses statement cancel, which may not always work on DB2 on z/OS because z/OS has limited support for canceling queries without disrupting the connection.
  - Value 2: Closes the socket, which reliably interrupts the query but can be more aggressive (e.g., closes the connection).
  - If not set to 2 on z/OS, the timeout may be silently ignored or fail to interrupt the query.
- **Version-Specific Changes**: Between FP3 and FP8 of DB2 10.5, there were bug fixes and enhancements in the driver. Although no specific APAR directly ties to setQueryTimeout in these fix packs, upgrades in this range have been reported to resolve issues where setQueryTimeout failed to work in non-WebSphere environments (e.g., Tomcat), likely due to improved thread handling or interrupt logic. Earlier versions like 4.17.29 may ignore non-zero timeouts silently in some cases (especially on z/OS), while later versions like 4.19.66 are more reliable when the appropriate property is set.

#### Which One Works, Which Doesn't
- **4.17.29 (doesn't work reliably)**: In some setups, particularly with DB2 on z/OS or in Tomcat-like environments, setQueryTimeout may not enforce the timeout as expected. It can be silently ignored for non-zero values, or the timer thread may hang without interrupting the query. This has been reported in older driver versions, leading to applications hanging on long-running queries.
- **4.19.66 (works)**: This version includes fixes from subsequent fix packs, making setQueryTimeout more reliable. It works as expected when configured properly, especially if queryTimeoutInterruptProcessingMode is set to 2 for z/OS connections. Upgrading to this version has resolved timeout issues in cases where older versions failed.

#### Why the Difference
The difference stems from bug fixes and improvements in the driver between DB2 10.5 FP3 and FP8. Older versions had known issues with timeout enforcement in certain configurations (e.g., thread contention or platform-specific limitations on z/OS, where statement cancel isn't always supported). Later fix packs addressed these, improving compatibility and reliability. Additionally, for DB2 on z/OS, the driver in newer versions better enforces the need for property configuration to avoid silent failures. If your application is on z/OS, the default interrupt mode (statement cancel) may not work in either version without setting the property to close socket mode; however, the newer version handles the overall logic better due to updates.

To make setQueryTimeout work in both versions (especially on z/OS):
 - Set the connection property `queryTimeoutInterruptProcessingMode=2` in the JDBC URL or DataSource.
 - Example URL: `jdbc:db2://host:port/database:queryTimeoutInterruptProcessingMode=2;`
 - Always use the latest driver within a release for bug fixes.

If the issue persists, enable driver tracing (using db2.jcc.traceDirectory property) to debug.

### References
- JDBC DB2 queryTimeout not working as expected (Stack Overflow) (https://stackoverflow.com/questions/59931952/jdbc-db2-querytimeout-not-working-as-expected)
- IBM Data Server Driver for JDBC and SQLJ configuration properties (https://www.ibm.com/docs/en/db2-for-zos/12.0.0?topic=information-data-server-driver-jdbc-sqlj-configuration-properties)
- PK86019 APAR Details (https://www.ibm.com/support/pages/apar/PK86019)
- JDBC driver version evolution (https://angocadb2.blogspot.com/2014/08/jdbc-driver-version-evolution.html)
- Db2 JDBC Driver Versions and Downloads (https://www.ibm.com/support/pages/db2-jdbc-driver-versions-and-downloads)